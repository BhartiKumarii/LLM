from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=OllamaLLM(model="gemma:2b",num_predict=100,temperature=0.5)
content = """
    The solar system consists of the Sun, eight planets, their moons, dwarf planets, and smaller objects like asteroids and comets. 
    The inner planets—Mercury, Venus, Earth, and Mars—are rocky and solid. 
    The outer planets—Jupiter, Saturn, Uranus, and Neptune—are much larger and gaseous.
"""

question = "Which planets in the solar system are rocky and solid?"


prompt = PromptTemplate(input_variables=["content","question"],
                        template = """
    Answer the {question} based on the {content}.
    Respond "Unsure about answer" if not sure about the answer.
    
    Answer:
    
""")

parser = StrOutputParser()
chain= prompt | llm | parser
response=chain.invoke({"content":content,"question":question})
print(f"prompt: {prompt.format(content=content, question=question)}\n")
print(f"response : {response}\n")