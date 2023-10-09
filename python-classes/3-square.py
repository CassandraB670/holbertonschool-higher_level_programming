#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """Empty class Square that defines a square with size."""
    def __init__(self, size=0):
        """Instantiate a square with size

        Args:
            size of the square, default = 0
        Raises:
            TypeError if size isn't an integer
            ValueError if size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
