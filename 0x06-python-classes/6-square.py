#!/usr/bin/python3
"""Square related feature module."""


class Square:
    """Class that define a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """
            Args:
                size (int): size initializer
                position (tuple): a tuple of two positive integer
        """
        self.__size = None
        self.__position = None

        self.size = size
        self.position = position

    def area(self):
        """Compute the area of the Square.

            Returns:
                The area. An (integer)
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """__size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """__size property setter.

            Args:
                value (int): new size value

            Raises:
                TypeError: if `value` is not an integer
                ValueError: if `value` is < 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """__position proper getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """__position property setter"""
        if not (
                type(value) is tuple and
                len(value) == 2 and
                type(value[0]) is int and
                type(value[1]) is int and
                value[0] >= 0 and
                value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Draw the square to the stdout"""
        x = " " * self.__position[0]
        y = "\n" * self.__position[1]

        if self.__size == 0:
            print()
            return

        print(y, end="")
        for i in range(self.__size):
            print(x + "#" * self.__size)
