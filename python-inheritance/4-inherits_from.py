#!/usr/bin/python3
"""write a function that returns True if the object is an instance of
a class that inherited from, the specified class"""


def inherits_from(obj, a_class):
    """write a function that returns True if the object is an instance of
a class that inherited from, the specified class

    Args:
        obj :objet
        a_class : class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
