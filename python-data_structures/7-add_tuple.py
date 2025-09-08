#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = [0, 0]
    for i in range(len(tuple_c)):
        if (i < len(tuple_a)):
            tuple_c[i] += tuple_a[i]
        if (i < len(tuple_b)):
            tuple_c[i] += tuple_b[i]
    tuple_c = tuple(tuple_c)
    return tuple_c
