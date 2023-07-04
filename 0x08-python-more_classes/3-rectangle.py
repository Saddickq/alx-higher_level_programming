#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """ Initialisation method """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Getter method """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value

    @property
    def width(self):
        """ Getter method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an integer")
        self.__width = value

    def area(self):
        """ Public instance method """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Public instance method """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """ String method """
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = ""
        for _ in range(self.__height):
            shape += '#' * self.__width
            shape += '\n'
        return (shape.rstrip())
