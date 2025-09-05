#!/usr/bin/python3
for i in range(100):
    print("{num:02d}".format(num=i), end="\n" if i == 99 else ", ")
