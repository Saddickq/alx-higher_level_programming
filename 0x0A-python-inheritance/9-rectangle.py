#!/usr/bin/python3
"""
A defined called BaseGeometry class
"""


class BaseGeometry:
    """A BaseGeometry class"""

    def area(self):
        """
        public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        """
        public instance method
        """

        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """ Area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ str method """
        return ("[Rectangle] {}/{}" .format(self.__width, self.__height))
