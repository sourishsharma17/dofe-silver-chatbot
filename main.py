from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = input("Enter prompt > ")


stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# a stream is a concept in programming/internet
# taking in a constant flow of data from the internet and showing it to the user



"""
Homework:
(10-15 mins)
- What is an LLM? --> A large language model (LLM) is a type of artificial intelligence (AI) program that can recognize and generate text, among other tasks.

- What are tokens? --> Tokens can be thought of as pieces of words.

- Explain the basic mechanism for how LLMs generate text. --> Recurrent layers, feedforward layers, embedding layers, and attention layers work in tandem to process the input text and generate output content.

(5 mins)
- What is git used for? --> Git is a DevOps tool used for source code management.
- What is Github? --> GitHub is a developer platform that allows developers to create, store, manage and share their code.
"""


