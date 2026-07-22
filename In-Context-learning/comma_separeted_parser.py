from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser


llm=OllamaLLM(model="gemma:2b",num_predict=80,temperature=0.5)

output_parser = CommaSeparatedListOutputParser()

prompt = PromptTemplate(
    template=(
        "List five {subject} as a single line of comma separated values, "
        "e.g. vanilla, chocolate. "
        "Do not number them or add any preamble, explanation, or bullet points."
    ),
    input_variables=["subject"],
)
chain = prompt | llm |  output_parser

response=chain.invoke({"subject": "ice cream flavors"})
print(response)