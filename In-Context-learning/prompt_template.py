from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
llm=OllamaLLM(model="gemma:2b",temperature=0.5,num_predict=256)

template = """Tell me a {adjective} joke about {content}.
"""
prompt = PromptTemplate.from_template(template)



#response=llm.invoke(prompt.format(adjective="funny", content="doctor"))
def format_prompt(variables):
    return prompt.format(**variables)

joke_chain = (
    RunnableLambda(format_prompt)
    | llm 
    | StrOutputParser()
)
response = joke_chain.invoke({"adjective": "funny", "content": "Doctor"})
print(response)