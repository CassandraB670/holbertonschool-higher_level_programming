#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """Empty class Square that defines a square with size."""
    def __init__(self, size=0):
        """Instantiate a square with size

        Args:
            size of the square, default = 0
        """
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """return size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): size of the square

        Raises:
            TypeError: if value isn't an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
