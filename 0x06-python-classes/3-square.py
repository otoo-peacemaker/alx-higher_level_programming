#!/usr/bin/python3
"""Square related feature module."""


class Square:
    """Class that define a Square."""

    def __init__(self, size=0):
        """
            Args:
                size (int): size initializer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Compute the area of the Square.

            Returns:
                The area. An (integer)
        """

        return (self.__size ** 2)
