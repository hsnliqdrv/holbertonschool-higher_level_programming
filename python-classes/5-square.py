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

    def area(self):
        """Computes area of square

        Returns:
            int: Area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter for the size of the square

        Returns:
            int: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size

        Arguments:
            value (int): new value of size
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def my_print(self):
        """Prints the square using # character
        """
        print("\n".join(["#" * self.size] * self.size))
