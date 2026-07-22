from langchain_ollama import OllamaLLM
llm=OllamaLLM(model="gemma:2b",num_predict=10)

prompt = """Here are few examples of classifying emotions in statements:

            Statement: 'I just won my first marathon!'
            Emotion: Joy
            
            Statement: 'I can't believe I lost my keys again.'
            Emotion: Frustration
            
            Statement: 'My best friend is moving to another country.'
            Emotion: Sadness
            
            Now, classify the emotion in the following statement:
            Statement: 'That movie was so scary I had to cover my eyes.’
            

"""
response = llm.invoke(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")