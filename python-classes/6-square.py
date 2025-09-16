#!/usr/bin/python3
"""1-square

This module includes a square class
"""


class Square:
    """Defines a square

    Attributes:
        __size (int) - size of the square
    """
    def __init__(self, size=0, position=(0,0)):
        """Initializes a square

        Arguments:
            size (int) - size of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes area of square

        Returns:
            int: Area of the square
        """
        return (self.size) ** 2

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

    @property
    def position(self):
        """Getter for the position

        Returns:
            tuple(int,int): position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position

        Arguments:
            value (tuple(int,int)): new value of position
        """
        if (type(value) is not tuple or len(value) != 2 or
            type(value[0]) is not int or type(value[1]) is not int or 
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using # character
        """
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
