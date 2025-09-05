#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = number % 10 if number >= 0 else (10 - number % 10)
print("Last digit of", number, "is", k, "and", end=" ")
if (k > 5):
    print("is greater than 5")
elif (k == 0):
    print("is 0")
else:
    print("is less than 6 and not 0")
