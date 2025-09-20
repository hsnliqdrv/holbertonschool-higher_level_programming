#!/usr/bin/python3
"""0-rectangle

This module provides a Rectangle class
"""


class Rectangle:
    """Defines a rectangle

    Attributes:
        width (int): width of rect
        height (int): height of rect
    """
    def __init__(self, width=0, height=0):
        """Initializer for rectangle

        Arguments:
            width (int): width
            height (height): height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute

        Returns:
            int: width of rect
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute

        Arguments:
            value (int): new value for width
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute

        Returns:
            int: height of rect
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute

        Arguments:
            value (int): new value for height
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Finds Area of rectangle

        Returns:
            int: area (a * b)
        """
        return self.width * self.height

    def perimeter(self):
        """Find perimeter

        Returns:
            int: perimeter
        """
        if (self.width == 0 or self.height == 0):
            return 0
        return (self.width + self.height) * 2
