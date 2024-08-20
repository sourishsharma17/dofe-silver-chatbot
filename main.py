# HOMEWORK:
# https://platform.openai.com/docs/concepts
# read this heading: Text generation models
# read this heading: Tokens

# Question 1
# i) fill in the gap ________ to make the code work:
def add_numbers(a, b):
    result = a + b
    print(result)

add_numbers(5, 11)


# ii) fill in the gap _______ to make the code work, and fix the syntax error:
def average(a, b):
    total = a + b
    avg = total / 2
    return avg

ans = average(45, 35)
print(ans)


# Question 2
# i) add Emma's score of 95 to the 'grades' dictionary below (without modifying the line of code)
# ii) print bob's grade to the screen 
# (you might need to reference the code in backup.py, or Google to remind yourself of dictionaries)

grades =  {"Alice": 85, "Bob": 92, "Charlie": 78}
grades["Emma"] = 95


# Question 3
# Write a loop that prints the numbers 1 to 100.

num = range(1,101)
for i in num:
    print(i)


# Now modify it to print only 1, 3, 5, ... 97, 99
# There are two ways to do this - can you get both?

#1
num = range(1,101)
for i in num:
    if i % 2 != 0:
        print(i)

#2
num = range(1, 101, 2)
for i in num:
        print(i)
        

# Question 4
# Write a loop that goes through this list and only prints the even numbers
numbers = [3, 7, 12, 5, 9, 18]

for i in numbers:
    if i % 2 == 0:
        print(i)


# Question 5
# Use a loop to add all of the numbers in the list below (and print the answer to the screen)
# (the code in archive.py might help ONLY IF you are stuck)

nums = [2, 10, 43, 3, 9]

total = 0
for num in nums:
    total = num + total
    print(total)


# Question 6
# Find the 2nd largest number in this list (and print it). Do NOT just sort the list, find another way ;)


nums = [10, 5, 20, 8] 


largest = float('-inf') #I don't know what ('-inf') means
for num in nums:
    if num > largest:
        largest = num

second_largest = float('-inf')
for num in nums:
    if num > second_largest and num < largest:
        second_largest = num

print(second_largest)


# Question 7
# Write code which creates (and prints) a new list, where each element is replaced by the sum of the 2 (or 1) elements next to it.
# ! remember to make sure it's generalised (i.e. works with a different input list) !


nums = [10, 20, 30, 40]  
# expted output: [20, 40, 60, 30]

new_list =[]
for i in range(len(nums)):
    if i == 0:
        new_list.append(nums[i + 1])
    elif i == len(nums) - 1:
        new_list.append(nums[i - 1])
    else:        
        new_list.append(nums[i - 1] + nums[i + 1])
print(new_list)

