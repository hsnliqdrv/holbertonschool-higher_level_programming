#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (97 <= ord(str[i]) < 97 + 26):
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(str[i]), end="")
    print()
