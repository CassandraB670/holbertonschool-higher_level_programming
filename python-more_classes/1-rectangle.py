#!/usr/bin/python3

"""class Rectanlge that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle with width and height."""
    def __init__(self, width=0, height=0):
        """rectangle width private optional instance attribute

        Args:
            width of the rectangle, default = 0
            height of the rectangle, default = 0
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value (int): size of the rectangle

        Raises:
            TypeError: if value isn't an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """return width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int): size of the rectangle

        Raises:
            TypeError: if value isn't an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
