#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        end = "\n" if i == len(str) - 1 else ""
        if (97 <= ord(str[i]) < 97 + 26):
            print("{}".format(chr(ord(str[i]) - 32)), end=end)
        else:
            print("{}".format(str[i]), end=end)
