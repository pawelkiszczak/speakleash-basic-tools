# speakleash-basic-tools
A collection of SpeakLeash tools used in the project.

## Web Crawler - `crawler_custom.py`
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

### License
This project is licensed under MIT License.
