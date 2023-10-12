#!/usr/bin/python3
"""define a function add_integer(a, b=98) that adds 2 integers"""


def add_integer(a, b=98):
    """add 2 integers

    Args:
        a(int): First value
        b(int): second value, default to 98.

    Raises:
        TypeError : if a and b are not integers or floats.

    Returns:
        Int Sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
