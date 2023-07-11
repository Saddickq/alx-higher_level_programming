#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry


""" A defined class called Rectangle"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from the
    BaseGeometry class
    """
    def __init__(self, width, height):
        """ init method """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
