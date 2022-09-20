#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """Geomerty utility class"""

    def area(self):
        """Returns the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle geometry class"""

    def __init__(self, width, height):
        """Sets the width and height of a Rectangle instance

            width (int): The width of the Rectangle
            height (int): The height of the Rectange
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """``area`` method implemenation for Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string description of the Rectangle"""
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__width, self.__height)
