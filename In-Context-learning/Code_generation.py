from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=OllamaLLM(model="gemma:2b",num_predict=100,temperature=1)
description = """
    Retrieve the names and email addresses of all customers from the 'customers' table who have made a purchase in the last 30 days. 
    The table 'purchases' contains a column 'purchase_date'
"""


template=PromptTemplate(input_variables=["description"],
                        template = """
    Generate an SQL query based on the {description}
    
    SQL Query:
    
"""
 )
parse=StrOutputParser()

chain= template | llm | parse
response=chain.invoke({"description": description})
print(f"prompt:{template.format(description=description)}\n")
print(f"response:{response}")
