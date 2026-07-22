from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=OllamaLLM(model="gemma:2b",num_predict=100,temperature=1)
text = """
    The concert last night was an exhilarating experience with outstanding performances by all artists.
"""

categories = "Entertainment, Food and Dining, Technology, Literature, Music."
template=PromptTemplate(input_variables=["text","categories"],
                        template = """
    Classify the {text} into one of the {categories}.
    
    Category:
    
""")
parse=StrOutputParser()

chain= template | llm | parse
response=chain.invoke({"text":text,"categories":categories})
print(f"prompt:{template.format(text=text,categories=categories)}\n")
print(f"response:{response}")
