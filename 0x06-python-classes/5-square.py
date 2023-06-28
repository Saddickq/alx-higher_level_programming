#!/usr/bin/python3
"""define an class Square"""


class Square:
    """A class with private instance attribute"""

    def __init__(self, size=0):
        """Intialise data"""
        self.__size = size

    @property
    def size(self):
        """A property to retrieve the attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """A property to set thee attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public instance method for finding the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """public instance method for printing"""
        if self.__size == 0:
            print()
        else:
            for _ in range(0, self.__size):
                for _ in range(0, self.__size):
                    print("#", end="")
                print()
