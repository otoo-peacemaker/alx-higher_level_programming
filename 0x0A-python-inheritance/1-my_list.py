#!/usr/bin/python3
"""The ``MyList`` module"""


class MyList(list):
    """MyList inherting from the ``list`` class"""

    def print_sorted(self):
        """Print the list as sorted"""
        print(sorted(self))
