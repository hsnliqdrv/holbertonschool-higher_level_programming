#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub  # 3
    if (a < b):  # 4
        c = add(a, b)  # 5
        for i in range(4, 6):  # 6
            c = add(c, i)  # 7
        return c  # 8
    return sub(a, b)  # 10
