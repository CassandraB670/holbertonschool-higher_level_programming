#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """Empty class Square that defines a square with size."""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a square with size

        Args:
            __size (int): size of the square
            __position (tuple): position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ return position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square position

        Args:
            value (int): position of the square

        Raises:
            TypeError: if value isn't a tuple of 2 integers
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Print the square with character # in stdout"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for i in range(self.__position[0])]
            [print("#", end="") for i in range(self.__size)]
            print("")
