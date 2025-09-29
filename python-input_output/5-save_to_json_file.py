#!/usr/bin/python3
"""5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves object to file as json

    Arguments:
        my_obj (object): object to serialize
        filename (str): string repr of obj
    """
    data = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(data)
