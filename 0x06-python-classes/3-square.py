#!/usr/bin/python3
"""define an class Square"""


class Square:
    """A class with private instance attribute"""

    def __init__(self, size=0):
        """Instantiation with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A method that gives the area of an object"""
        return (self.__size ** 2)
