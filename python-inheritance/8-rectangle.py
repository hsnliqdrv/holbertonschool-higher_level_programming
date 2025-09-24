#!/usr/bin/python3
"""8-rectangle

This module provides a rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle

    Attributes:
        width (int): width of rect
        height (int): height of rect
    """

    def __init__(self, width, height):
        """Initializer of rectangle

        Arguments:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
