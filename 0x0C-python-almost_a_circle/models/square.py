#!/usr/bin/python3
"""``Square`` class module"""

from .rectangle import Rectangle


class Square(Rectangle):
    """A class that represent a Square"""

    def __init__(self, size, x=0, y=0, _id=None):
        """Initialize the Square's instance.

            Args:
                size (int): The size of the Square
                x (int): The x position of the Square
                y (int): The y position of the Square
                _id (any): The id of the instance object
        """
        super().__init__(size, size, x, y, _id)

    def __str__(self):
        """Returns a string representation of the Square's instance"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Returns the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the `width` and `height` of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the instance's attributes"""
        attrs = ("id", "size", "x", "y")
        if args:
            len_args = len(args)
            len_attrs = len(attrs)
            if len_args > len_attrs:
                msg = "update() takes at max {} positional arguments"\
                        " but {} were given"
                raise TypeError(msg.format(len_attrs, len_args))

            for i in range(len_args):
                setattr(self, attrs[i], args[i])
        else:
            for k in kwargs:
                if k not in attrs:
                    msg = "update() got an unexpected keyword argument '{}'"
                    raise TypeError(msg.format(k))
                setattr(self, k, kwargs.get(k))

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
