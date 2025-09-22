#!/usr/bin/python3
"""0-lookup

This module provides the lookup function
"""


def lookup(obj):
    """Gives all available methods and
    attributes of an object

    Returns:
        list[string]: List of attributes and methods
    """
    return dir(obj)
