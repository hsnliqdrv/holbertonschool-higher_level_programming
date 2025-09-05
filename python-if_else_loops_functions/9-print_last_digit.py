#!/usr/bin/python3
def print_last_digit(number):
    k = number % 10 if number >= 0 else 10 - number % 10
    print(k, end="")
    return k
