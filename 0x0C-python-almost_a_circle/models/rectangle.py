#!/usr/bin/python3
"""``Rectangle`` class module"""


from .base import Base


class Rectangle(Base):
    """A class that represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, _id=None):
        """Sets new Rectangle's instance fields

            Args:
                width (int): The width of the Rectangle
                height (int): The height of the Rectangle
                x (int): The position x of the Rectangle
                y (int): The position y of the Rectangle
                id (any): The id of the instance object
        """
        super().__init__(_id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_dimension_attr(name, value):
        """Validate the dimension attributes: `width` and `height`.
            Raise an Error if not valid
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def validate_position_attr(name, value):
        """Validate the position attributes: `x` and `y`"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        Rectangle.validate_dimension_attr("width", value)
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        Rectangle.validate_dimension_attr("height", value)
        self.__height = value

    @property
    def x(self):
        """Returns the position x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the position x"""
        Rectangle.validate_position_attr("x", value)
        self.__x = value

    @property
    def y(self):
        """Returns y position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y position"""
        Rectangle.validate_position_attr("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """
            Prints in stdout the Rectangle instance
            With the character `#`.
        """
        x, y, w, h = self.x, self.y, self.width, self.height
        print("\n" * y + (" " * x + "#" * w + "\n") * h, end="")

    def __str__(self):
        """
            Returns a string representation of the Rectangle:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attrs = ("id", "width", "height", "x", "y")
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
        """Returns the ditionary representation of a Rectangle"""
        return {'y': self.y,
                'x': self.x,
                'id': self.id,
                'width': self.width,
                'height': self.height}
