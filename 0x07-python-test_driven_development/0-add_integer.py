#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(). For example,
>>> add_integer(10, 12)
"""


def add_integer(a, b=98):
    """
        Adds two integer.
        Args:
            a (int|float): An integer or floating point number
            b (int|float): An integer or floating point number
        Returns: The sum of `a` and `b`
    """

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not int:
        raise TypeError("b must be an integer")

    return (a + b)
