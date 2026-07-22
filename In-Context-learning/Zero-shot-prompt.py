from langchain_ollama import OllamaLLM
llm=OllamaLLM(model="gemma:2b",num_predict=256,temperature=0.5,top_p=0.2,top_k=1)

prompt1 = """Classify the following statement as true or false: 
            'The Eiffel Tower is located in Berlin.'

            Answer:
"""
prompt2="""Classify the following statement as Positive or negative:
           'I love the Graphics and climax scene of the Movie!'
           Answer:"""

prompt3="""Summarize a Paragraph about Climate Change"""

prompt4="""Translate the Following English Sentence to Spanish:
         'Good,Morning'
         Answer"""
chunks=[prompt1,prompt2,prompt3,prompt4]
for chunk in chunks:
    print(f"prompt: {chunk}\n")
    print("response : ", end="", flush=True)
    [print(token, end="", flush=True) for token in llm.stream(chunk)]
    print("\n")