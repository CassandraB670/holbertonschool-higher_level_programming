#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle with width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """rectangle width optional instance attribute

        Args:
            width of the rectangle, default = 0
            height of the rectangle, default = 0
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance

        Args:
            cls : using for access class attribute
            size (int, optional): size of the rectangle Defaults to 0.
        """
        return Rectangle(size, size)

    def __str__(self):
        """Print a rectangle using #

        returns: rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for index in range(self.__height):
            for index2 in range(self.__width):
                rectangle.append(str(self.print_symbol))
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

    def __del__(self):
        """
        Print a message when an instance is deleted

        Returns:
            str: Bye rectangle...
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1 (int): first rectangle
            rect_2 (int): second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 >= area2:
            return rect_1
        else:
            return rect_2
