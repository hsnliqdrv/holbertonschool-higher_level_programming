#!/usr/bin/python3
"""4-from_json_string
"""
import json


def from_json_string(my_str):
    """From JSON to object

    Arguments:
        my_str (str): a json string

    Returns:
        (object): object represented by string
    """
    return json.loads(my_str)
