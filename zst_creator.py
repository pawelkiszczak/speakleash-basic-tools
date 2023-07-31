import multiprocessing
import os
import shutil
import json
import glob
import time
from lm_dataformat import Archive
from ttictoc import tic, toc
from multiprocessing import Manager
from itertools import repeat

# CONFIG
TXT_DIR = "your-txt-dir-here/"
###

def process_item(item, counter, total_files):
    """
    Process an individual text file and return its content and metadata.

    Parameters:
        item (str): The path of the text file to process.
        counter (Value): A shared counter to keep track of processed files.
        total_files (int): The total number of files to be processed.

    Returns:
        tuple: A tuple containing the processed text and its metadata.
    """
    counter.value += 1
    with open(item, "r", encoding="utf-8") as f:
        txt = f.read()
    print("Processing file:", item, counter.value, "/", total_files,
          round((counter.value / total_files * 100), 2), "%")
    l = len(txt)

    item = item.replace(TXT_DIR, "")
    meta = {'name': item, 'length': l}
    return txt.strip(), meta

if __name__ == '__main__':
    tic()
    # Manager is optional, used to properly iterate 'counter' variable with multithreading
    # function only return the percentage of completion of given dataset
    manager = Manager()
    counter = manager.Value('i', 0)
    ar = Archive('./data')
    data = None

    with open(f"{TXT_DIR}/temp.json", 'r') as jf:
        data = json.load(jf)

    file_name_zst = './data/' + data.get("name", "") + '.jsonl.zst'
    file_name_manifest = './data/' + data.get("name", "") + '.manifest'

    print(file_name_zst, file_name_manifest)

    txt_files = [os.path.join(TXT_DIR, file) for file in os.listdir(TXT_DIR) if file.endswith(".txt")]
    total_files = len(txt_files)

    total_len = 0
    total_docs = 0

    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        results = pool.starmap(process_item,
                               zip(txt_files,
                                   repeat(counter),
                                   repeat(total_files)),
                               chunksize=os.cpu_count() - 1)
        for txt, meta in results:
            total_len += meta['length']
            total_docs += 1
            ar.add_data(txt.strip(), meta=meta)
        ar.commit()

    data_files = glob.glob('./data/*')
    file_size = 0

    ar = None

    for f in data_files:
        if f.endswith('.zst'):
            shutil.copy(f, os.path.join(file_name_zst))
            file_size = os.path.getsize(file_name_zst)

        os.remove(f)

    manifest = {
        "project": data.get("project", ""),
        "name": data.get("name", ""),
        "description": data.get("description", ""),  # Fixed typo in the key name
        "license": data.get("license", ""),
        "language": data.get("language", ""),
        "file_size": file_size,
        "category": data.get("category", ""),
        "sources": data.get("sources", []),
        "stats": {
            "documents": total_docs,
            "sentences": 0,
            "words": 0,
            "nouns": 0,
            "verbs": 0,
            "characters": total_len,
            "punctuations": 0,
            "symbols": 0,
            'stopwords': 0,
            'oovs': 0
        }
    }
    json_manifest = json.dumps(manifest, indent=4)

    with open(file_name_manifest, 'w') as mf:
        mf.write(json_manifest)

    print(toc())