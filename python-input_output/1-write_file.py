#!/usr/bin/python3
"""1-write_file
"""


def write_file(filename="", text=""):
    """Writes string to a text file

    Arguments:
        filename (str): path to the file
        text (str): string to write to file

    Returns:
        (int): number of characters written
    """
    with open(filename, "w") as file:
        return file.write(text)
