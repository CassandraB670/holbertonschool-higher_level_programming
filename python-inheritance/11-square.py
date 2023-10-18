#!/usr/bin/python3
"""Write a class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """instantiation with size

        Args:
            size (int): size of the square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area of the square"""
        return self.__size ** 2

    def __str__(self):
        """print and return the square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
