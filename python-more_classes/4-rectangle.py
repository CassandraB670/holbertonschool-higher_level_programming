#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle with width and height."""
    def __init__(self, width=0, height=0):
        """rectangle width optional instance attribute

        Args:
            width of the rectangle, default = 0
            height of the rectangle, default = 0
        """
        self.height = height
        self.width = width

    def area(self):
        """returns the current rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the current rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

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

    def __str__(self):
        """Print a rectangle using #

        returns: rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for index in range(self.__height):
            for index2 in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
