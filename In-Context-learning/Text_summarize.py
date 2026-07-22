from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm=OllamaLLM(model="gemma:2b",num_predict=256,temperature=0.5,top_p=0.2,top_k=1)

content = """
    The rapid advancement of technology in the 21st century has transformed various industries, including healthcare, education, and transportation. 
    Innovations such as artificial intelligence, machine learning, and the Internet of Things have revolutionized how we approach everyday tasks and complex problems. 
    For instance, AI-powered diagnostic tools are improving the accuracy and speed of medical diagnoses, while smart transportation systems are making cities more efficient and reducing traffic congestion. 
    Moreover, online learning platforms are making education more accessible to people around the world, breaking down geographical and financial barriers. 
    These technological developments are not only enhancing productivity but also contributing to a more interconnected and informed society.
"""
template=PromptTemplate(input_variables=["content"],
                        template="""Summarize the following paragraph in 2-3 sentences:{content} Summary:
                        """)
parser = StrOutputParser()
chain = template | llm | parser
response=chain.invoke({"content": content})
print(f"prompt: {template.format(content=content)}\n")
print(f"response : {response}\n")