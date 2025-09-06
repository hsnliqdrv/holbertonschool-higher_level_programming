#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    c = len(argv) - 1
    print("{} argument".format(c), end="")
    if (c == 0):
        print("s.")
    elif (c == 1):
        print(":")
    else:
        print("s:")
    for i in range(1, c + 1):
        print("{}: {}".format(i, argv[i]))
