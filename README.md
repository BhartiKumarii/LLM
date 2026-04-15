# 📚 LLM Learning Journey

My learning repository for understanding Large Language Models (LLMs) and LangChain.

## What am I Learning?

I'm learning how to:
- 🤖 Use LLMs (Large Language Models)
- ⛓️ Build chains with LangChain
- 💬 Write good prompts
- 🔧 Process text with AI
- 🎯 Understand how AI models work

## Setup (First Time)

### What you need:
- Python 3.9+
- Ollama (free, runs locally)

### 1. Install Ollama
Go to: https://ollama.ai and download

### 2. Download a Model
```bash
ollama pull gemma:2b
3. Start Ollama
bash
ollama serve
This runs in background. Keep it running!

4. Install Python Package
bash
pip install langchain langchain-ollama
Folder Structure
Code
LLM/
├── intro_to_prompting/
│   └── Basic LLM examples (where I started)
│
└── chains/
    └── Advanced examples (practicing now)
What I'm Practicing
Basic Stuff (intro_to_prompting/)
Starting Simple:

llama.py - First example, just call the model
work1.py - Another simple example
work2.py - Generate text about space
Learning to Stream:

streaming.py - See output word by word
Processing Multiple Items:

Batching.py - Ask multiple questions at once
Batching1.py - Batch with different format
Using Templates:

template1.py - Simple template
template2.py - Translation template
template3.py - Extract information
template4.py - More translation
template5.py - Chat template
Analyzing Text:

Sentiment_analysis.py - Is it positive/negative?
Main_topic_identification.py - What's the main topic?
followup_question_generation.py - Generate follow-up questions
Security (Important!):

injection.py - How to break prompts (attack example)
iterative.py - Ask multiple questions in sequence
Chains (chains/)
Learning LangChain:

LCEL.py - LangChain basics
runnables.py - Make reusable components
OutputParser.py - Get structured output
RunnableLambda.py - Use custom functions
Building Chains:

combining_chain.py - Chain operations together
parallel_chain.py - Run multiple things at same time
Exercise.py - Translation chain (my first exercise!)
practice.py - More complex example
Simple Example (Start Here!)
1. First Program
Python
from langchain_ollama import OllamaLLM

# Connect to local model
llm = OllamaLLM(
    model="gemma:2b",
    base_url="http://localhost:11434"
)

# Ask a question
answer = llm.invoke("What is machine learning?")
print(answer)
Save as test.py and run:

bash
python test.py
You should see an answer!

2. Use a Template
Python
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma:2b", base_url="http://localhost:11434")

# Create a template
template = PromptTemplate.from_template(
    "Translate this to Spanish: {text}"
)

# Use it
chain = template | llm
result = chain.invoke({"text": "Hello world"})
print(result)
3. Ask Multiple Questions
Python
questions = [
    "What is AI?",
    "What is ML?",
    "What is Deep Learning?"
]

responses = llm.batch(questions)

for q, r in zip(questions, responses):
    print(f"Q: {q}")
    print(f"A: {r}\n")
4. Stream Output
Python
# See output appear word by word
for chunk in llm.stream("Tell me about Python"):
    print(chunk, end="", flush=True)
Files I'm Working On
Just Starting
intro_to_prompting/llama.py ← Start here
intro_to_prompting/work2.py ← Fun facts
Learning Templates
intro_to_prompting/template1.py ← Very simple
intro_to_prompting/template2.py ← Translation
intro_to_prompting/template4.py ← More translation
Learning to Process Multiple
intro_to_prompting/Batching.py ← Process many items
Learning Chains
chains/LCEL.py ← LangChain basics
chains/runnables.py ← Make reusable code
chains/OutputParser.py ← Get clean output
Common Things I'm Learning
✅ What Works
Python
# Simple call
llm.invoke("question")

# With template
template | llm

# Multiple questions
llm.batch(questions)

# Stream output
llm.stream("question")
❌ Common Mistakes
Python
# Wrong: Ollama not running
# Fix: Run "ollama serve" first

# Wrong: Model not downloaded
# Fix: Run "ollama pull gemma:2b"

# Wrong: Wrong base URL
# Fix: Use "http://localhost:11434"

# Wrong: Trying online API without key
# Fix: Use local Ollama for free
How to Run Each File
Simple files
bash
python intro_to_prompting/llama.py
python intro_to_prompting/streaming.py
python intro_to_prompting/Sentiment_analysis.py
Files with chains
bash
python chains/LCEL.py
python chains/OutputParser.py
python chains/runnables.py
My practice files
bash
python chains/Exercise.py
python chains/practice.py
What Each Concept Does
Prompts
Templates for asking questions

Python
template = PromptTemplate.from_template("Translate: {text}")
# Then use: template.invoke({"text": "hello"})
Chains
Connect multiple operations together

Python
chain = template | llm | parser
# Runs: template → llm → parser
Batching
Ask many questions at once

Python
llm.batch(["Q1", "Q2", "Q3"])
# Returns: [answer1, answer2, answer3]
Streaming
See output appear gradually

Python
for chunk in llm.stream("question"):
    print(chunk, end="")
# Prints: word word word...
Runnables
Reusable components

Python
from langchain_core.runnables import RunnableLambda
my_function = RunnableLambda(lambda x: x.upper())
My Learning Goals
 Understand how LLMs work
 Master LangChain basics
 Build simple chains
 Parse LLM output
 Process batches
 Build a real project
Useful Resources I'm Using
LangChain Tutorial: https://python.langchain.com/docs/get_started/introduction
Ollama: https://ollama.ai
YouTube tutorials on LangChain
OpenAI Prompt Engineering: https://platform.openai.com/docs/guides/prompt-engineering
Latest Files I'm Working On
intro_to_prompting/streaming.py - Learning to stream
chains/OutputParser.py - Learning to parse output
chains/RunnableLambda.py - Learning functions in chains
chains/parallel_chain.py - Learning parallel processing
Notes for Myself
Remember:

Ollama must be running (ollama serve)
Model must be downloaded (ollama pull gemma:2b)
Always use correct base_url: http://localhost:11434
LangChain is just a wrapper around LLMs
Chains make complex operations simple
Templates make prompts reusable
Quick Command Reference
bash
# Download model
ollama pull gemma:2b

# Start ollama (run in separate terminal)
ollama serve

# Install packages
pip install langchain langchain-ollama

# Run a file
python intro_to_prompting/llama.py

# Check if ollama works
curl http://localhost:11434/api/generate -d '{"model":"gemma:2b","prompt":"hi"}'
Author
Bharti Kumari - Learning LLMs 📚

GitHub: @BhartiKumarii
Learning since: Sept 2025
Current Focus
Right now I'm focusing on:

Understanding basic LLM calls ✅
Learning prompt templates ✅
Learning how to chain operations 🔄 (Working on this)
Building a simple project (Next)
