#!/usr/bin/python3
"""1-square

This module includes a square class
"""


class Square:
    """Defines a square

    Attributes:
        __size (int) - size of the square
    """
    def __init__(self, size=0):
        """Initializes a square

        Arguments:
            size (int) - size of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    pass
