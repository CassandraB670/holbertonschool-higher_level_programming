#!/usr/bin/python3
"""Write a function that returns the dictionary description
with simple data structure for JSON serialization of an object"""


def class_to_json(obj):
    """fct that returns the dictionary description

    Args:
        obj : instance of a class

    Return: dictionary description
    """
    return obj.__dict__
