#!/usr/bin/python3
"""0-read_file
"""


def read_file(filename=""):
    """Reads a text file and prints content

    Arguments:
        filename (str): the path to file
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
