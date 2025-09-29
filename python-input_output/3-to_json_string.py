#!/usr/bin/python3
"""3-to_json_string
"""
import json


def to_json_string(my_obj):
    """Return JSON of object

    Arguments:
        my_obj (object): an object

    Returns:
        (str): serialized object
    """
    return json.dumps(my_obj)
