#!/usr/bin/python3
"""2-is_same_class

This Module provides a function is_same_class
"""


def is_same_class(obj, a_class):
    """Checks if object is *exactly* an instance of class

    Returns:
        boolean: True if instance else False
    """
    return type(obj) is a_class
