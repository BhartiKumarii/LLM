from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=OllamaLLM(model="gemma:2b",num_predict=100,temperature=0.5)

role = """
    Dungeon & Dragons game master
"""

tone = "engaging and immersive"


prompt = PromptTemplate(input_variables=["role","tone"],
                    template = """
                  You are an expert {role}. I have this question {question}. I would like our conversation to be {tone}.
    
    Answer:
    
"""    )

parser=StrOutputParser()
chain=prompt | llm | parser
# Create an interactive chat loop
while True:
    query = input("Question: ")
    
    if query.lower() in ["quit", "exit", "bye"]:
        print("Answer: Goodbye!")
        break
        
    response = chain.invoke({"role": role, "question": query, "tone": tone})
    print("Answer: ", response)