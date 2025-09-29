#!/usr/bin/python3
"""9-student
"""


class Student:
    """Represents a Student
    """

    def __init__(self, first_name, last_name, age):
        """Initializer

        Arguments:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gives dictionary description

        Returns: (dict)
        """
        return self.__dict__
