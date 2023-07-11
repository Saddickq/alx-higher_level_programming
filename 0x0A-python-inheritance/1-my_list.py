#!/usr/bin/python3
"""
A module that inherits from a class and
prints a list in ascending order
"""


class MyList(list):
    """
    A class that inherits from the class list
    """

    def print_sorted(self):
        """
        Public instance method
        """

        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
