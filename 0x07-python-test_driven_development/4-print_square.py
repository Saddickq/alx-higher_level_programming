#!/usr/bin/python3

"""
module that prints a square
"""


def print_square(size=0):
    """A function that prints a square"""
    if (size == 0):
        return (None)
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
