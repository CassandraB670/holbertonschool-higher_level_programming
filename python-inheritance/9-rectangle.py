#!/usr/bin/python3
"""write a class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """instantiation with width and height

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print and return description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
