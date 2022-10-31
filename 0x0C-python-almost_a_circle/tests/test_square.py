#!/usr/bin/python
"""``Square`` testing module"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
import contextlib
import io


class TestSquare(unittest.TestCase):
    """Test cases for the `Square` class"""


    def test_inheritance(self):
        """Check if Square class inherit from Base class"""
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_missing_arguments(self):
        """Check required positional argument existance"""
        with self.assertRaises(TypeError) as cm:
            sqr = Square()
        except_msg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(cm.exception), except_msg)
        
    def test_normal_creation(self):
        """Test normal instantiation"""
        sqr = Square(10)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.height, 10)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)

        sqr = Square(7, 12, 13, 100)
        self.assertEqual(sqr.width, 7)
        self.assertEqual(sqr.height, 7)
        self.assertEqual(sqr.x, 12)
        self.assertEqual(sqr.y, 13)
        self.assertEqual(sqr.id, 100)

    def test_dimension_attributes_validation(self):
        """Test `width` and `height` validation"""

        with self.assertRaises(TypeError) as cm:
            sqr = Square("1")
        except_msg = "width must be an integer"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(ValueError) as cm:
            sqr = Square(0)
        except_msg = "width must be > 0"
        self.assertEqual(str(cm.exception), except_msg)

    def test_position_attributes_validation(self):
        """Test `x` and `y` validation"""

        with self.assertRaises(TypeError) as cm:
            sqr = Square(1,"0")
        except_msg = "x must be an integer"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(ValueError) as cm:
            sqr = Square(1,-1)
        except_msg = "x must be >= 0"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(TypeError) as cm:
            sqr = Square(1, 0, "0")
        except_msg = "y must be an integer"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(ValueError) as cm:
            sqr = Square(1,0, -1)
        except_msg = "y must be >= 0"
        self.assertEqual(str(cm.exception), except_msg)


    def test_area_method(self):
        """Test area method"""
        sqr = Square(5)
        self.assertEqual(sqr.area(), 25)

        sqr = Square(1)
        self.assertEqual(sqr.area(), 1)

        sqr = Square(8, 0, 0, 12)
        self.assertEqual(sqr.area(), 64)

    def test_display_on_dimension_change(self):
        """Test display stdout"""
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                sqr = Square(1)
                sqr.display()

                sqr = Square(5)
                sqr.display()

                sqr = Square(2)
                sqr.display()
            out = "#\n" + ("#" * 5 + "\n") * 5 + ("#" * 2 + "\n") * 2
            self.assertEqual(buf.getvalue(), out) 

    def test_display_on_position_change(self):
        """Test display when position `x` and `y` changes"""
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                sqr = Square(1, 2, 2)
                sqr.display()

                sqr = Square(5, 2, 0)
                sqr.display()

                sqr = Square(2)
                sqr.display()
            out = "\n\n  #\n" + ("  " + "#" * 5 + "\n") * 5 + ("#" * 2 + "\n") * 2
            self.assertEqual(buf.getvalue(), out) 

    def test_magic_str_method(self):
        """Test magic `__str__` method"""
        sqr = Square(4, 2, 1, 12)
        self.assertEqual(sqr.__str__(), "[Square] (12) 2/1 - 4")

        sqr = Square(5, 1)
        self.assertEqual(sqr.__str__(),
                "[Square] ({}) 1/0 - 5".format(sqr.id))


    def test_update_with_args(self):
        """Test update method with *args"""
        sqr = Square(5)

        self.assertEqual(sqr.__str__(),
                "[Square] ({}) 0/0 - 5".format(sqr.id)) 
        
        sqr.update(10)
        self.assertEqual(sqr.__str__(), "[Square] (10) 0/0 - 5")

        sqr.update(1, 2)
        self.assertEqual(sqr.__str__(), "[Square] (1) 0/0 - 2")

        sqr.update(1, 2, 3)
        self.assertEqual(sqr.__str__(), "[Square] (1) 3/0 - 2")

        with self.assertRaises(TypeError) as cm:
            sqr.update(1, 2, 3, 4, 5)
        except_msg = "update() takes at max 4 positional arguments"\
                " but 5 were given" 
        self.assertEqual(str(cm.exception), except_msg)

    def test_update_with_kwargs(self):
        """Test update moethod with **kwargs""" 
        sqr = Square(5, 0, 0, 1)

        self.assertEqual(sqr.__str__(),
                "[Square] (1) 0/0 - 5")

        sqr.update(size=1)
        self.assertEqual(sqr.__str__(), "[Square] (1) 0/0 - 1")

        sqr.update(y=3, x=2)
        self.assertEqual(sqr.__str__(), "[Square] (1) 2/3 - 1")

        with self.assertRaises(TypeError) as cm:
            sqr.update(width=3)
        except_msg = "update() got an unexpected keyword argument 'width'"
        self.assertEqual(str(cm.exception), except_msg)

    def test_to_dictionary_method(self):
        """Test to_dictionary method"""

        sqr = Square(10, 2, 1, 1)
        sqr_dict = sqr.to_dictionary()

        tups = [("id", 1), ("size", 10), ('x', 2), ('y', 1)]
        for k, v in tups:
            self.assertEqual(sqr_dict.get(k), v)

        sqr = Square(1,1)
        sqr.update(**sqr_dict)
        sqr_dict_2 = sqr.to_dictionary()
        for k, v in tups:
            self.assertEqual(sqr_dict.get(k), sqr_dict_2.get(k))

    def test_save_to_file_classmethod(self):
        """Test ``save_to_file`` classmethod on Square"""
        Square.save_to_file(None)

        saved = ""
        with open('Square.json', 'r', encoding="utf-8") as f:
                saved = f.read()
        self.assertEqual(saved, "[]")

        rect_1 = Square(10, 7, 2, 8)
        rect_2 = Square(2, 4)
        Square.save_to_file([rect_1, rect_2])

        with open('Square.json', 'r', encoding='utf-8') as f:
            saved = f.read()

        self.assertEqual(len(saved), 78)

    def test_load_from_file_classmethod(self):
        """Test ``load_from_file`` classmethod on Square"""

        sqrs = Square.load_from_file()
        self.assertEqual(type(sqrs) is list, True)

        if len(sqrs) > 0:
            for sqr in sqrs:
                self.assertEqual(isinstance(sqr, Square), True)

    def test_create_class_method(self):
        """Test ``create`` class method on Rectangle"""
        sqr = Square.create(**{'id': 89})
        self.assertEqual(sqr.id, 89)

        sqr = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 1)

        sqr = Square.create(**{'id': 89, 'size': 1, 'x': 3})
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 1)
        self.assertEqual(sqr.x, 3)

        sqr = Square.create(
                **{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 1)
        self.assertEqual(sqr.x, 3)
        self.assertEqual(sqr.y, 4)

