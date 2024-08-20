from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = input("Enter prompt > ")


stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt},
              {"role": "system", "content": "You are Albert Einstein. The year is 1920. You should exaggerate Einstein's characteristics."}],
    stream=True,
    temperature=1.0,
    max_tokens=4096
)

# tell me a story about two lovers whos' parents were enemies

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# a stream is a concept in programming/internet
# taking in a constant flow of data from the internet and showing it to the user
