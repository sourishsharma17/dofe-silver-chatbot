## chatbot ##
from openai import OpenAI
import os

Gerald = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

message_history = [
                   {"role": "system", "content": "Your name is Gerald. A quiz contestant will be asked a series of questions, and you must check to see if their responses are correct. Be lenient in how they communicate their answer; they may share a thought process or make a typo of the answer. For each question, only say 'Well done!' if they were correct, and only say 'YOU'RE WRONG!' once if they were wrong. Do not say anything else under any other circumstances. If the answer is wrong then give the quiz contestant the correct answer."}
                  ]

# answer = input("What is the capital of England? ")
score = 0
Qs = int(input("How many questions do you want to answer? "))
print("\033c", end="")


for _ in range(Qs):

    prompt = "Ask a question to the quiz contestant."

    message_history.append({"role": "user", "content": prompt})


    stream = Gerald.chat.completions.create(
        model="gpt-4o",
        messages=message_history,
        stream=True,
        temperature=1.5,
        max_tokens=1024
    )

    response = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            response += chunk.choices[0].delta.content

    message_history.append({"role": "assistant", "content": response})

    print()

    answer = input()

        
    prompt = f"Check the answer {answer}."

    message_history.append({"role": "user", "content": prompt})


    stream = Gerald.chat.completions.create(
        model="gpt-4o",
        messages=message_history,
        stream=True,
        temperature=1.5,
        max_tokens=1024
    )

    response = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            response += chunk.choices[0].delta.content

    message_history.append({"role": "assistant", "content": response})

    
    if response == "Well done!":
        score += 1
    
    print()
    print()
    print()

print("your score is:", score, "out of", Qs)











