# Web Crawler - `crawler_custom.py`
It's a Python web crawler that is designed to extract and save URLs from provided web pages. The crawler is built to work asynchronously using asyncio and httpx for making HTTP requests. It can be used to crawl web pages within certain domains and filter URLs based on specific criteria.

Script has been created by [@adgw](https://github.com/AdGw) and due to his courtesy I'm able to share it with you after some small tweaks.

### How it works
The web crawler consists of the following main components:
1. **UrlFilterer** (Class)
   - Responsible for filtering URLs basedon criteria such as allowed domains/schemes/filetypes/restricted URLs.
2. **UrlParser** (Class)
   - A custom HTML parser that extracts URLs from anchor tags (`<a>`) within HTML content.
   - Uses `UrlFilterer` to validate and filter extracted URLs.
3. **Crawler** (Class)
   - Represents the web crawler that initiates and manages the whole crawling process.
   - Uses an HTTP client provided by `httpx` for making asynchronous HTTP requests to fetch web page content.
   - The crawler starts with a list of starting URLs and continuously extracts URLs from pages, following links to new pages as long as the limit is not reached.
   - The fetched URLs are filtered using `UrlFilterer` with new URLs being added to queue for further processing.
4. **main** (function)
   - Entry point of the script that sets up the `UrlFilterer` based on the domain of the input URL.
   - Initializes the HTTP client and creates a `Crawler` with provided parameters.
   - Crawling starts with the `run()` method from the `Crawler` class.
  
### Configuration
The crawler is customizable with following variables:
* `WORKERS`: The number of worker tasks to run concurrently. By default it's set to the number of CPU cores available.
* `LIMIT`: The maximum number of URLs to crawl and extract.
* `CRAWLER_LIMIT`: The maximum number of URLs the crawler can process.
* `FILE`: The name of file containing a list of starting URLs. By default, it's set to `custom.txt`.

### Usage
To use the crawler, follow the steps below:
1. Create a `custom.txt` file (default name) containing the starting URLs to start the crawl from, one URL per line.
2. Make sure you have Python 3.7+ installed.
3. Install the required dependencies using `pip install httpx`
4. Run the crawler by executing the `custom_crawler.py` script
   ```bash
   python custom_crawler.py
   ```
   The crawler will start processing the URLs from `custom.txt` and extracted URLs will be saved to separate files named after their respective domains.

### Caution
* Always ensure that you have permission to crawl a website before running the script. Unauthorized or excessive crawling can lead to blocking IP address and other consequences.
* Use the script responsibly and always adhere to website's terms of service while crawling.
* The authors do not take responsibility of actions taken by users of forementioned script.

***

# Multi-threaded Archive creator - `zst_creator.py`
This script uses Python for multi-threaded processing of collected text data and creating a compressed archive with relevant metadata for the documents. It's designed to efficiently handle large amounts of text data and utilizes the `multiprocessing` library to achieve paraller processing.

The script has been created by [@jchwila](https://github.com/jchwila) and due to his courtesy I'm able to share it with you.

## Key features
* Utilizes multi-threading to process multiple files simultaneously for increased efficiency.
* Provides progress tracking to monitor processing of each file.
* Calculates and stores metadata for future postprocessing purposes.
* Cleans us after the process to ensure nothing was left behind and keep the workspace clean.

## Reqiurements
To run this script, you'll need to meet following dependencies:
* Python 3.x
* `lm_dataformat` (install using `pip install lm_dataformat`)
* `tictoc` (install using `pip install tictoc`)

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi-threaded-text-processing.git
   cd speakleash-basic-tools
   ```
2. Provide path to the directory where the text files are stored (`TXT_DIR` variable in config section)
3. Edit the `temp.json` file to match data about the texts you've gathered simply by replacing the asterisks (`*`). This file should be placed in the same directory as the text files.
4. Run the script:
   ```bash
   python zst_creator.py
   ```
After the script completes processing, you will find the compressed archive (`*.jsonl.zst`) and the manifest (`*.manifest`) files in the `./data/` directory.

## Configuration
Befere running the script, ensure you have configured the following variable:
* `TXT_DIR`: path to directory containing text files

## Output
* **Compressed Archive**: The processed text data is stored in the Language Model Data Format (LMDF) compressed archive.
* **Manifest file**: Contains metadata about the processed data (mostly a placeholder for future postprocessing).

***

### License
This project is licensed under MIT License.
