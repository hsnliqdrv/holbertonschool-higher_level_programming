#!/usr/bin/python3
"""6-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """Creates object from json file

    Arguments:
        filename (str): path to the file

    Returns:
        (object): object from file
    """
    with open(filename, "r") as file:
        return json.load(file)
