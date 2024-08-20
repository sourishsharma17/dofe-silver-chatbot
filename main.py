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
