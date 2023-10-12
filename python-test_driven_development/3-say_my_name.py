#!/usr/bin/python3
"""define a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """print My name is <first name> <last name>

    Args:
        first_name(string): First value
        last-name(string): second value, default to "".

    Raises:
        TypeError : if first_name and last_name aren't strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
