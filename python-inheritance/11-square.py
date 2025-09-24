#!/usr/bin/python3
"""10-square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square

    Attributes:
        size (int): size of square
    """

    def __init__(self, size):
        """Initializer

        Arguments:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area

        Returns:
            (int): square of size
        """
        return self.__size ** 2

    def __str__(self):
        """String representation

        Returns:
            (str): string repr
        """
        return "[Square] {0}/{0}".format(self.__size)
