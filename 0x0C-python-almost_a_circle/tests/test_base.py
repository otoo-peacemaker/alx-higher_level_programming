#!/usr/bin/python3
"""``Base`` class test module"""

import unittest
import inspect

from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test case for the Base class model"""

    def test_create(self):
        """Test if required private attribute exist"""
        inst_1 = Base()
        inst_2 = Base()
        inst_3 = Base(10)
        self.assertEqual(inst_1.id, 1)
        self.assertEqual(inst_2.id, 2)
        self.assertEqual(inst_3.id, 10)

    def test_to_json_string(self):
        """Test ``to_json_string`` static method"""

        isstatic = isinstance(
                inspect.getattr_static(Base, "to_json_string"), staticmethod)
        self.assertEqual(isstatic, True)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        self.assertEqual(
                Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

        except_msg = "list_dictionaries must be a list of dictionaries"

        with self.assertRaises(TypeError) as cm:
            Base.to_json_string("not a dictionary")
        self.assertEqual(str(cm.exception), except_msg)

        with self.assertRaises(TypeError) as cm:
            Base.to_json_string([{'id': 1, 'width': 4}, 12])
        self.assertEqual(str(cm.exception), except_msg)

    def test_from_json_string(self):
        """Test ``from_json_string`` static method"""
        isstatic = isinstance(
                inspect.getattr_static(Base, "from_json_string"), staticmethod)
        self.assertEqual(isstatic, True)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

        list_dicts = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(type(list_dicts) is list, True)
        self.assertEqual(len(list_dicts) == 1, True)
        self.assertEqual(type(list_dicts[0]) is dict, True)
