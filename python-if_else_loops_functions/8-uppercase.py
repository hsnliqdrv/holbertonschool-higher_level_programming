#!/usr/bin/python3
def toupper(char):
    if (97 <= ord(char) < 97 + 26):
        return chr(ord(char) - 32)
    return char


def uppercase(str):
    for i in range(len(str)):
        print("{}".format(toupper(str[i])), end="")
    print()
