#!/usr/bin/python3
"""1-my_list

This module provides MyList class
"""


class MyList(list):
    """Inheritance of built-in list
    """

    def print_sorted(self):
        """Prints list in ascending order
        """
        print(sorted(self))
