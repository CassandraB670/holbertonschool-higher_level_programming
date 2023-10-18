#!/usr/bin/python3
"""write a function that returns True if the object
is exactly an instance of the specified class or False"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class

    Args:
        obj :objet
        a_class : _class

    Return : True or False
    """
    return type(obj) is a_class
