#!/usr/bin/python
"""``Rectangle`` testing module"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import contextlib
import io


class TestRectangle(unittest.TestCase):
    """Test cases for the `Rectangle` class"""

    def test_inheritance(self):
        """Check if Rectangle class inherit from Base class"""
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_missing_arguments(self):
        """Check required positional argument existance"""

        with self.assertRaises(TypeError) as cm:
            rect = Rectangle()
        except_msg = "__init__() missing 2 required positional arguments: "\
                    "'width' and 'height'"
        self.assertEqual(str(cm.exception),except_msg)

        with self.assertRaises(TypeError) as cm:
            rect = Rectangle(10)
        except_msg = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(cm.exception), except_msg)

    def test_normal_creation(self):
        """Test normal instantiation"""
        rect = Rectangle(10, 51)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 51)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        rect = Rectangle(10, 7, 12, 13, 100)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 12)
        self.assertEqual(rect.y, 13)
        self.assertEqual(rect.id, 100)

    def test_dimension_attributes_validation(self):
        """Test `width` and `height` validation"""

        with self.assertRaises(TypeError) as cm:
            rect = Rectangle("1", 1)
        except_msg = "width must be an integer"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(ValueError) as cm:
            rect = Rectangle(0, 1)
        except_msg = "width must be > 0"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(TypeError) as cm:
            rect = Rectangle(1, "1")
        except_msg = "height must be an integer"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(ValueError) as cm:
            rect = Rectangle(1, 0)
        except_msg = "height must be > 0"
        self.assertEqual(str(cm.exception), except_msg)

    def test_position_attributes_validation(self):
        """Test `x` and `y` validation"""

        with self.assertRaises(TypeError) as cm:
            rect = Rectangle(1, 1, "0")
        except_msg = "x must be an integer"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(ValueError) as cm:
            rect = Rectangle(1, 1, -1)
        except_msg = "x must be >= 0"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(TypeError) as cm:
            rect = Rectangle(1, 1, 0, "0")
        except_msg = "y must be an integer"
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(ValueError) as cm:
            rect = Rectangle(1, 1, 0, -1)
        except_msg = "y must be >= 0"
        self.assertEqual(str(cm.exception), except_msg)

    def test_area_method(self):
        """Test area method"""
        rect = Rectangle(5, 5)
        self.assertEqual(rect.area(), 25)

        rect = Rectangle(1, 1)
        self.assertEqual(rect.area(), 1)

        rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect.area(), 56)

    def test_display_on_dimension_change(self):
        """Test display stdout"""
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                rect = Rectangle(1, 1)
                rect.display()

                rect = Rectangle(5, 10)
                rect.display()

                rect = Rectangle(2, 2)
                rect.display()
            out = "#\n" + ("#" * 5 + "\n") * 10 + ("#" * 2 + "\n") * 2
            self.assertEqual(buf.getvalue(), out)

    def test_display_on_position_change(self):
        """Test display when position `x` and `y` changes"""
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                rect = Rectangle(1, 1, 2, 2)
                rect.display()

                rect = Rectangle(5, 10, 2, 0)
                rect.display()

                rect = Rectangle(2, 2)
                rect.display()
            out = "\n\n  #\n" + ("  " + "#" * 5 + "\n") * 10 + ("#" * 2 + "\n") * 2
            self.assertEqual(buf.getvalue(), out)

    def test_magic_str_method(self):
        """Test magic `__str__` method"""
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rect.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        rect = Rectangle(5, 5, 1)
        self.assertEqual(rect.__str__(),
                "[Rectangle] ({}) 1/0 - 5/5".format(rect.id))

    def test_update_with_args(self):
        """Test update method with *args"""
        rect = Rectangle(10, 10, 10, 10)

        self.assertEqual(rect.__str__(),
                "[Rectangle] ({}) 10/10 - 10/10".format(rect.id))
       
        rect.update(89)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        rect.update(89, 2)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        rect.update(89, 2, 3)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        rect.update(89, 2, 3, 4)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        with self.assertRaises(TypeError) as cm:
            rect.update(89, 2, 3, 4, 5, 6)
        except_msg = "update() takes at max 5 positional arguments but 6 were given"
        self.assertEqual(str(cm.exception), except_msg)

    def test_update_with_kwargs(self):
        """Test update moethod with **kwargs"""
        rect = Rectangle(10, 10, 10, 10, 1)

        self.assertEqual(rect.__str__(),
                "[Rectangle] (1) 10/10 - 10/10")

        rect.update(height=1)
        self.assertEqual(rect.__str__(), "[Rectangle] (1) 10/10 - 10/1")

        rect.update(width=1, x=2)
        self.assertEqual(rect.__str__(), "[Rectangle] (1) 2/10 - 1/1")

        rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 3/1 - 2/1")

        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 1/3 - 4/2")

        with self.assertRaises(TypeError) as cm:
            rect.update(xyz=1)
        except_msg = "update() got an unexpected keyword argument 'xyz'"
        self.assertEqual(str(cm.exception), except_msg)

    def test_to_dictionary_method(self):
        """Test to_dictionary method"""
        rect = Rectangle(10, 2, 1, 9, 1)
        rect_dict = rect.to_dictionary()

        self.assertEqual(str(type(rect_dict)), "<class 'dict'>")
        tups = [('id', 1), ('width', 10), ('height', 2), ('x', 1), ('y', 9)]
        for k, v in tups:
            self.assertEqual(rect_dict.get(k), v)

        rect = Rectangle(1, 1)
        rect.update(**rect_dict)
        rect_dict_2 = rect.to_dictionary()
        for k, v in tups:
            self.assertEqual(rect_dict.get(k), rect_dict_2.get(k))

    def test_create_class_method(self):
        """Test ``create`` class method on Rectangle"""
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual(rect.id, 89)

        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

        rect = Rectangle.create(
                **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_save_to_file_classmethod(self):
        """Test ``save_to_file`` classmethod on Rectangle"""
        Rectangle.save_to_file(None)

        saved = ""
        with open('Rectangle.json', 'r', encoding="utf-8") as f:
                saved = f.read()
        self.assertEqual(saved, "[]")

        rect_1 = Rectangle(10, 7, 2, 8)
        rect_2 = Rectangle(2, 4)
        Rectangle.save_to_file([rect_1, rect_2])

        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            saved = f.read()

        self.assertEqual(len(saved), 107)

    def test_load_from_file_classmethod(self):
        """Test ``load_from_file`` classmethod on Rectangle"""

        rects = Rectangle.load_from_file()
        self.assertEqual(type(rects) is list, True)

        if len(rects) > 0:
            for rect in rects:
                self.assertEqual(isinstance(rect, Rectangle), True)
