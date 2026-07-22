# Import the WebBaseLoader class from langchain_community's document_loaders module
# This loader is designed to scrape and extract text content from web pages
from langchain_community.document_loaders import WebBaseLoader

# Create a WebBaseLoader instance by passing the URL of the web page to load
# This URL points to the LangChain documentation's introduction page
loader = WebBaseLoader("https://python.langchain.com/v0.2/docs/introduction/")

# Call the load() method to:
# 1. Send an HTTP request to the specified URL
# 2. Download the HTML content
# 3. Parse the HTML to extract meaningful text
# 4. Create a list of Document objects containing the extracted content
web_data = loader.load()

# Print the first 1000 characters of the page content from the first Document
# This provides a preview of the successfully loaded web content
# web_data[0] accesses the first Document in the list
# .page_content accesses the text content of that Document
# [:1000] slices the string to get only the first 1000 characters
print(web_data[0].page_content[:1000])