from random import randint
from time import sleep

while True:
  lst = [randint(0, 9),
         randint(0, 9),
         randint(0, 9),
         randint(0, 9)]



  nums = "".join([str(num) for num in lst])

  print(nums)
  sleep(1)
  print("\033c", end="")

  ans = input("Please enter the numbers: ")



  if ans == nums:
    print("Well done!!!")
  else:
    print("WRONG, the correct answer was:", nums)

  answer = input("Do you want to play again? (y/n) ")
  if answer == "y":
    continue
  else:
    print("Thank you for playing!!")
    break




















# Q1: print the length of each name using a loop
names = ["Gary", "Bob", "Timothy"]

for i in names:
  print(len(i))


# Q2: use a loop and print only the items where there are at least 3 of
inventory = {"apples": 5, "bananas": 2, "oranges": 7}

for i in inventory.keys():
  if inventory[i] >= 3:
    print(i)


# Q3: Ask the user for a number and print the sum of the digits in that number
# e.g. input: 149, output: 14

#num = input("Please enter a number: ")
num = "432552345"

total = 0
for i in num:
  total = total + int(i)

print(total)


# Q4: Ask the user for 2 numbers, and use a loop to print out all of the common divisors of the two numbers
# e.g. input: 30 and 36
# output: 1, 2, 3, 6













from random import randint
from time import sleep


lst = [randint(0, 9),
       randint(0, 9),
       randint(0, 9),
        randint(0, 9),
        randint(0, 9),
        randint(0, 9),
      randint(0, 9),
       randint(0, 9)]



nums = "".join([str(num) for num in lst])

print(nums)
sleep(1)
print("\033c", end="")

ans = input("Please enter the numbers: ")



if ans == nums:
  print("Well done!!!")

print(nums)


###############




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

