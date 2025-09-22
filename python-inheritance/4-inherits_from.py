#!/usr/bin/python3
"""4-inherits_from

This module provides a function inherits_from
"""
def inherits_from(obj, a_class):
    """Check if obj's class inherited from a_class

    Returns:
        boolean: true if inherited else false
    """
    b_class = obj.__class__
    return a_class != b_class and issubclass(b_class, a_class)
