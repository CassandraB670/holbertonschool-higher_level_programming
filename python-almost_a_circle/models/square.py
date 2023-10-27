#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits form class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """print representation str of the Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
