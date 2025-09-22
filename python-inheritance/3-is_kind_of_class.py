#!/usr/bin/python3
"""3-is_kind_of_class

This module provides a function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of a class

    Returns:
        boolean: True if instance else False
    """
    return isinstance(obj, a_class)
