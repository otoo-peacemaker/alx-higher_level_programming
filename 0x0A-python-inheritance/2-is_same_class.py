#!/usr/bin/python3
"""Module to check if object are of same class"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of the specified class"""
    return type(obj) is a_class
