#!/usr/bin/python3
"""7-base_geometry
"""


class BaseGeometry:
    """This class represents base Geometric shapes
    """

    def area(self):
        """Calculate area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value

        Arguments:
            name (str): name
            value (int): value
        """
        if (type(value) != int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
