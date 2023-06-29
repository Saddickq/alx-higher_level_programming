#!/usr/bin/python3
"""define an class Square"""


class Square:
    """A class with private instance attribute"""

    def __init__(self, size=0):
        """Intialise data"""
        self.size = size

    @property
    def size(self):
        """method that returns private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Instantiation with size"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if (value < 0):
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """A method that gives the area of an object"""
        return (self.__size ** 2)
