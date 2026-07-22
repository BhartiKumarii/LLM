from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

llm=OllamaLLM(model="gemma:2b",num_predict=100,temperature=0.5)
msg=llm.invoke( [
        SystemMessage(content="You are a helpful AI bot that assists a user in choosing the perfect book to read in one short sentence"),
        HumanMessage(content="I enjoy mystery novels, what should I read?")
    ])
print(msg)

msg1 = llm.invoke(
    [
        SystemMessage(content="You are a supportive AI bot that suggests fitness activities to a user in one short sentence"),
        HumanMessage(content="I like high-intensity workouts, what should I do?"),
        AIMessage(content="You should try a CrossFit class"),
        HumanMessage(content="How often should I attend?")
    ]
)
print(msg1)