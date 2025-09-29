#!/usr/bin/python3
"""8-class_to_json
"""


def class_to_json(obj):
    """Convert class instance to dictionary

    Arguments:
        obj (object): an object

    Returns:
        (dict): dictionary description
    """
    return obj.__dict__
