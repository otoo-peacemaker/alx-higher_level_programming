#!/usr/bin/python3
"""``MyInt`` rebelious class module"""


class MyInt(int):
    """``MyInt`` class with `==` and `!=` operators inverted"""

    def __eq__(self, instance):
        """checks if self == instance but inverted"""
        return super().__ne__(instance)

    def __ne__(self, instance):
        """checks if self != instance but inverted"""
        return super().__eq__(instance)
