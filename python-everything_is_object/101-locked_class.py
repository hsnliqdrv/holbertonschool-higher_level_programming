#!/usr/bin/python3
"""101-locked_class

This module implements LockedClass
"""


class LockedClass:
    """This class is locked"""
    def __setattr__(self, name, value):
        """Only allow to set attribute 'first_name'

        Arguments:
            name (string): name of attribute
            value (object): value of attribute
        """
        if name != 'first_name':
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
