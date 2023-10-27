#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """_summary_
        """
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

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """_summary_
        """
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

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """_summary_"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the height of the rectangle

        Args:
            value (int): size of the rectangle

        Raises:
            TypeError: if value isn't an integer
            ValueError: if value is < 0
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """_summary_"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the height of the rectangle

        Args:
            value (int): size of the rectangle

        Raises:
            TypeError: if value isn't an integer
            ValueError: if value is < 0
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """print the Rectangle instance with # in stdout"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """print representation str of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribtue"""
        if args:
            attributs = [self.id, self.width, self.height, self.x, self.y]
            for index, arg in enumerate(args):
                if index < len(attributs):
                    setattr(self, attributs[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
