from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

Document(page_content="""Python is an interpreted high-level general-purpose programming language.
 Python's design philosophy emphasizes code readability with its notable use of significant indentation.""",
metadata={
    'my_document_id' : 234234,                      # Unique identifier for this document
    'my_document_source' : "About Python",          # Source or title information
    'my_document_create_time' : 1680013019          # Unix timestamp for document creation (March 28, 2023)
 })
loader = PyPDFLoader("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/96-FDF8f7coh0ooim7NyEQ/langchain-paper.pdf")
document = loader.load()
document[2]
print(document[1].page_content[:1000])
