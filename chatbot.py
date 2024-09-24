
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


message_history = [
                   {"role": "system", "content": "You are a 40 year old british king."}
                  ]

while True:

    #print(message_history)

    prompt = input("Enter prompt > ")

    message_history.append({"role": "user", "content": prompt})



    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=message_history,
        stream=True,
        temperature=1.0,
        max_tokens=1024
    )

    response = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            response += chunk.choices[0].delta.content

    message_history.append({"role": "assistant", "content": response})


    print()
    print()



