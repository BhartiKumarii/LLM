from langchain_ollama import OllamaLLM
llm=OllamaLLM(model="gemma:2b",num_predict=256,temperature=0.5,top_p=0.2,top_k=1)

prompt1 = "The wind is "
prompt2="The future of artificial intelligence is"
prompt3="Once upon a time in a distant galaxy"
prompt4="The benefits of sustainable energy include"

# Getting a reponse from the model with the provided prompt and new parameters

chunks=[prompt1,prompt2,prompt3,prompt4]
for chunk in chunks:
    print(f"prompt: {chunk}\n")
    print("response : ", end="", flush=True)
    [print(token, end="", flush=True) for token in llm.stream(chunk)]
    print("\n")