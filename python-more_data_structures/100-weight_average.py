#!/usr/bin/python3
def weight_average(my_list=[]):
    if (not my_list):
        return 0
    s, n = 0, 0
    for number, weight in my_list:
        s += number * weight
        n += weight
    return s / n
