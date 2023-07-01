#!/usr/bin/python3
"""
A module that adds two numbers
"""
def add_integer(a, b=98):
    """A function that add two numbers
        parameters:
        a(int): first arguments
        b(int): second arguments

        raise: TypeErrors if non-integers
        return: sum of a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
