#!/usr/bin/python3
"""2-append_write
"""


def append_write(filename="", text=""):
    """Appends text to file

    Arguments:
        filename (str): path to file
        text (str): text to be written

    Returns:
        (int): number of characters written
    """
    with open(filename, "a") as file:
        return file.write(text)
