#!/usr/bin/python3
"""4-print_square

This module includes a function print_square
"""


def print_square(size):
    """Prints a square of size 'size'

    Argument 'size' must be a non-negative integer
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    print('\n'.join(["#" * size] * size))
