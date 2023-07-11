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

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
