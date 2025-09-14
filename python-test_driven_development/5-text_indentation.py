#!/usr/bin/python3
"""5-text_indentation

This module includes a function text_indentation
"""


def text_indentation(text):
    """Prints two newline characters after each ?, . or :

    Argument must be a string
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    line = ""
    for ch in text:
        line += ch
        if ch in '?.:':
            print(line.strip(), end='\n\n')
            line = ""
    print(line.strip(), end="")
