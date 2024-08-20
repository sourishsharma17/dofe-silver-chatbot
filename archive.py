# Write a loop that prints each element in a given list
# now write a program that calculates the sum of every element in a list, and then prints out the answer
lst = [10, 7, 2, 400, 600]

total = 0

for num in lst:
  total = num + total


print(total)





# Convert these 2 lists into a dictionary:
keys_list = ['Ten', 'Twenty', 'Thirty', 'Forty']
values_list = [10, 20, 30, 40]

# output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


numbers = {}


for num in range(len(key_list)):
  numbers[keys_list[num]] = values_list[num]


print(numbers)


