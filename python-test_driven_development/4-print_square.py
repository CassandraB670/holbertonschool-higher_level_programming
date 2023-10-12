#!/usr/bin/python3
"""define a function that prints a square with the character #"""


def print_square(size):
    """print a square with the character #

    Args:
        size(int): First value

    Raises:
        TypeError: if size isn't an integer
        TypeError: if size is less than 0
        ValueError: if size is a float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for index in range(size):
        print("#" * size)
