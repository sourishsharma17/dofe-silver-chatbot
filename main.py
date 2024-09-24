## chatbot ##
from openai import OpenAI
import os

Gerald = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

message_history = [
                   {"role": "system", "content": "Your name is Gerald. A user was asked a question, 'What is the capital of England?', and you must check to see if their response was correct. Be lenient in how they communicate their asnwer. Only say 'Well done!!!!!!!' if they were correct, and only say 'YOU'RE WRONG!!!!!!!!!!!!' once if they were wrong. Do not say anything else under any other circumstances."}
                  ]

answer = input("What is the capital of England? ")


while True:

    #print(message_history)

    #prompt = input("Enter prompt > ")

    message_history.append({"role": "user", "content": answer})


    stream = Gerald.chat.completions.create(
        model="gpt-4o",
        messages=message_history,
        stream=True,
        temperature=0.5,
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
    break








