#!/usr/bin/python3
"""define an class Square"""


class Square:
    """A class with private instance attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Intialise data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """A property to retrieve the attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """A property to set thee attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """A property to retreive attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter for the private instance attribute, position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public instance method for finding the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """public instance method for printing"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
