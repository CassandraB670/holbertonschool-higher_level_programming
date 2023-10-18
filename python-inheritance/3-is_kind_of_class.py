#!/usr/bin/python3
"""write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from, the specified
class"""


def is_kind_of_class(obj, a_class):
    """write a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from, the
    specified class

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Return : True of False
    """

    return isinstance(obj, a_class)
