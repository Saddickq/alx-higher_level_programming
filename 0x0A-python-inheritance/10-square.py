#!/usr/bin/python3
"""
A defined class called Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the
    Rectangle class
    """
    def __init__(self, size):
        """ init method """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Area method """
        return (self.__size * self.__size)

    def __str__(self):
        """ the str() """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
