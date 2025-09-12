#!/usr/bin/python3
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(roman_string):
    if (type(roman_string) is not str):
        return 0
    s = 0
    for i in range(len(roman_string)):
        s += d[roman_string[i]]
        if (i > 0 and d[roman_string[i - 1]] < d[roman_string[i]]):
            s -= 2 * d[roman_string[i - 1]]
    return s
