#!/usr/bin/python3
"""
    This is the ``4-print_square`` module.
    The 4-print_square module supplies one function, print_square().
"""


def print_square(size):
    """Prints a square with the character '#'.

        Args:
            size (int): The size length of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((('#' * size) + '\n') * size, end=("" if size else "\n"))
