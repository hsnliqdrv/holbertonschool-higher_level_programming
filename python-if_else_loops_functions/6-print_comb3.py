#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if (i == j):
            continue
        print("{}{}".format(i, j), end="\n" if i == 8 else ", ")
