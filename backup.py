# Quiz Game

quest = input("What is the capital of England? ")

#if quest == "London" or quest == "london" or quest == "the city of london":

if "london" in quest.lower():
  print("Well done!!!!!!!!!")
else:
  print("YOU'RE WRONG!")





# Q1: Write a program which goes through a list of numbers and outputs the results when every even number is multiplied together.

nums = [2, 3, 5, 6, 7, 10, 13, 14]
# expected output: 1680 (becuase 2*6*10*14 = 1680)

total = 1

for i in nums:
    if i % 2 == 0:
        total *= i

print(total)

# Q2: Now output the sum of the squares of the list.

#nums = [2, 3, 5, 6, 7, 10, 13, 14]
# expected output: 588 (becuase 4+9+25+36+49+100+169+196 = 588)


nums = [2, 3, 5, 6, 7, 10, 13, 14]

# list comprehension
total = sum(num ** 2 for num in nums)
print(total)

total = 0
for num in nums:
    total += num **2

print(total)



# Q3: ask the user for a sentence and output the number of vowels in the sentence
# example input:   "hello world!"
# expected output: 3

sentence = input("Please enter a sentence: ")

vowels = "aeiouAEIOU"

vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print("Number of vowels is:", vowel_count)



# Q4: Write a program which goes through a list of numbers and prints the numbers which are divisible by both 3 and 5.
lst = [15, 25, 10, 30, 45, 20, 50]
# expected output: 15, 30, 45

lst = [15, 25, 10, 30, 45, 20, 50]

for num in lst:
    if num % 3 == 0 and num % 5 == 0:
        print(num)



# Q5: Write a program which goes through a list of numbers and creates a new list without any duplicates.
lst = [1, 2, 3, 2, 4, 1, 5]
# expected output: [1, 2, 3, 4, 5]

lst = [1, 2, 3, 2, 4, 1, 5]

dif_lst = []
for num in lst:
    if num not in dif_lst:
        dif_lst.append(num)

print(dif_lst)











# Q4: Ask the user for 2 numbers, and use a loop to print out all of the common divisors of the two numbers
# e.g. input: 30 and 36
# output: 1, 2, 3, 6

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

for small_num in range(1, min(num1, num2) + 1):
  if num1 % small_num == 0 and num2 % small_num == 0:
    print(small_num)









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

