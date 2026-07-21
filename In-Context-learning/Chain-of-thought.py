from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="gemma:2b")

params = {
    "max_new_tokens": 512,
    "temperature": 0.5,
}

prompt1 = """Consider the problem: 'A store had 22 apples. They sold 15 apples today and got a new delivery of 8 apples. 
            How many apples are there now?’

            Break down each step of your calculation

"""
prompt2="""Consider the problem: I have upcoming Exam after two days But my friends are saying to go for a movie tonight. should i study or go for movie tonight?.

Break down The condition and give me solution"""

prompt3="""Consider Yourself a Chef: you have peanuts and sandwitch,and you know how to make peanuts butter and jelly sandwitch.

Now describe your Receipe in step by step process"""

chunks=[prompt1,prompt2,prompt3]
for chunk in chunks:
    print(f"prompt: {chunk}\n")
    print("response : ", end="", flush=True)
    [print(token, end="", flush=True) for token in llm.stream(chunk)]
    print("\n")