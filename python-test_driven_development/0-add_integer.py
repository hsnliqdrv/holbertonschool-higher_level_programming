#!/usr/bin/python3
"""0-add_integer.py

This module includes a function for adding two integers
"""


def add_integer(a, b=98):
    """Add two integers

    Arguments can be float or int.
    If float they are casted to int

    Sum of two integers is returned
    """
    if (type(a) not in [float, int]):
        raise TypeError("a must be an integer")
    if (type(b) not in [float, int]):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
