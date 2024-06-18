# TelegramAIParser
 
**Description**
This script is used to extract the content from a Telegram post and analyze it with provoded prompt using LM Studio Server and OpenAI's Chat Completion API.

**Usage**

1. Install and run LM Studio Server with desired model. [LM Studio Server Link.](https://lmstudio.ai)
2. Install required libraries by running `pip install requests beautifulsoup4 openai`
3. Set up your API credentials:
	* `open_ai` - set it to `"open_ai"`
	* `api_base` - set it to the base URL of your local OpenAI API, e.g., `"http://localhost:1234/v1"`
	* `api_key` - no need to set this up for local testing
3. Run the script by executing the Python file

**Code Overview**

The code consists of two main parts:

1. **Telegram post scraping**: Uses the `requests` and `beautifulsoup4` libraries to extract the content from a Telegram post.
2. **Analysis generation**: Uses OpenAI's Chat Completion API to generate a response based on the provided prompt.

**Variables**

* `url`: The URL of the webpage to scrape
* `headers`: Custom headers for the HTTP request
* `description_ tags`: A list of meta tags with og:description property
* `description`: The final description string with AI prompt for analysis
* `openai_api_type`, `api_base`, and `api_key`: API credentials

**Methods**

* `requests.get()`: Sends an HTTP GET request to the specified URL
* `BeautifulSoup()` : Parses the HTML content of a webpage
* `find_all()` : Finds all meta tags with og:description property
* `get('content')` : Retrieves the content of the first meta tag
* `openai.ChatCompletion.create()` : Creates a new chat completion request

**Error Handling**

* If the HTTP request returns a status code other than 200, an error message is printed.
* If no description tags are found, an error message is printed.

**Output**

The final generated response is printed to the console.