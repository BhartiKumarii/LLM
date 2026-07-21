from langchain_ollama import OllamaLLM
llm=OllamaLLM(model="gemma:2b")

params = {
    "max_new_tokens": 128,
    "temperature": 0.5,
}

prompt1 = """Here is an example of translating a sentence from English to French:

            English: “How is the weather today?”
            French: “Comment est le temps aujourd'hui?”
            
            Now, translate the following sentence from English to French:
            
            English: “Where is the nearest supermarket?”
            
"""

prompt2="""Here is an format of how to write an Email:
         
         TO:example@gmail.com
         subject:Submission of Assignment
         
         Dear sir,
         I have attached the given assignment and solved every questions.please review and give me feedback
         
         Thanks
         Regards
         BHarti
         
         Now, Write an email to HR for Resign
"""

prompt3="""Here is an example to explain technical Concepts into simple explanation:
          Technical Concept :Cloud in IT
          simple Explanation :it is someone else machine that store your data like AWS,Azure
          
          Now, EXplain Techincal Concepts of Database Normalization
"""
prompt4="""Here is an example of extracting keywords from a sentence:
        Sentence: I live in Delhi and started my job in 2021
        Keywords: Place: Delhi, Year: 2021

        Now, extract keywords from the following sentence:
        Sentence: you are eligible for this subsidy in Telangana but it will not commence after 2026
        Keywords:
"""

chunks=[prompt1,prompt2,prompt3,prompt4]
for chunk in chunks:
    print(f"prompt: {chunk}\n")
    print("response : ", end="", flush=True)
    [print(token, end="", flush=True) for token in llm.stream(chunk)]
    print("\n")