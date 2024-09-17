from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


while True:


    prompt = input("Enter prompt > ")


    message_history = [{"role": "system", "content": "You talk like a 15 year old british teenager."},
                       {"role": "user", "content": prompt}
                ]

    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=message_history,
        stream=True,
        temperature=1.0,
        max_tokens=1024
    )


    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

    print()
    print()


