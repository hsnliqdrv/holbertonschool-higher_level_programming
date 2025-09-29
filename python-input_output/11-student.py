#!/usr/bin/python3
"""11-student
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

    def to_json(self, attrs=None):
        """Gives dictionary description

        Returns: (dict)
        """
        d = self.__dict__
        if (type(attrs) is list and all(type(x) is str for x in attrs)):
            return dict([item for item in d.items() if item[0] in attrs])
        return d

    def reload_from_json(self, json):
        """Reload attributes from json object

        Arguments:
            json (dict): dictionary
        """
        for key in json.keys():
            self[key] = json[key]
