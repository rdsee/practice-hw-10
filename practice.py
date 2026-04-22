#Modules
import random
# from random import *
# from random import randint, choice

print(random.randint(1,100)) #random numbers

print(random.choice("qwerty")) # random symbols

print(random.randrange(10)) #random nums in range
print(random.randrange(1, 30))
print(random.randrange(1, 30, 2))

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)# random position in list
print(nums)

