#!/usr/bin/python3
"""defines a function for return a list"""


def lookup(obj):
    """function for return the list of available attributes
    and methods of an object

    Args:
        obj : object

    Return:
        list of attributes and methods
    """
    return dir(obj)
