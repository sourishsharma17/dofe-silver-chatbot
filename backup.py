#dictionary
# you can associate the value with a key

book = {
  'name': 'To Kill a Mockingbird',
  'capital': 'Harper Lee',
  'population': 1960,
  'language': 'Fiction'
}
print(book)


print(f"Title: {book['title']}")
print(f"Author: {book['author']}")


#functions
# code that you keep using without writing it all out

def is_even(number):
    if number % 2 = 0:
        return True
    else:
        return False

print(is_even(4))


#API
# a way of communicating and getting data from a server somewhere in the world (by sending a URL request)

import requests

api_key = '47c8fb92c2457c5b75dc80c6b0099da9'
city = 'London,uk'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'

response = requests.get(url)
weather_data = response.json()

print(f"Weather in {city}: {weather_data['weather'][0]['description']}")


#Write a report of what you remember about Dictionary, Fuctions and API


# Function: Write a function that returns the sum of all even numbers in a given list.
# example input: [1, 2, 4, 6, 7, 9]
# example output: 12


"""
Homework:
(10-15 mins)
- What is an LLM? --> A large language model (LLM) is a type of artificial intelligence (AI) program that can recognize and generate text

- What are tokens? --> Tokens can be thought of as pieces of words.

- Explain the basic mechanism for how LLMs generate text. --> It looks at the tokens its generated so far, and predicts the most likely token to appear next based off how humans talk.

(5 mins)
- What is git used for? --> Git is a DevOps tool used for source code management.

- What is Github? --> GitHub is a developer platform that allows developers to create, store, manage and share their code.
"""

