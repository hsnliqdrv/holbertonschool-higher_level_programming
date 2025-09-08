#!/usr/bin/python3
def no_c(my_string):
    return "".join([char for char in my_string if not char in 'cC'])
