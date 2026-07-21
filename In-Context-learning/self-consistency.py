from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3.2:1b")

params = {
    "max_new_tokens": 512,
}

prompt = """When I was 6, my sister was half of my age. Now I am 70, what age is my sister?

            Provide three independent calculations and explanations, then determine the most consistent result.

"""
response = llm.invoke(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")