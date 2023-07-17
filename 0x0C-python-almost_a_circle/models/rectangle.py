#!/usr/bin/python3
"""
A defined class called Rectangle that
inherits from the Base class
"""


from .base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constuctor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter method for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter method for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter method for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter method for x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter method for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter nethod for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ public method called area """
        return (self.__width * self.__height)

    def display(self):
        """ public method to display the rectangle """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ string representation """
        msg = "[Rectangle] ({}) {}/{} - {}/{}"
        return (msg.format(self.id, self.__x, self.__y,
                self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Public method """
        if args:
            try:
                self.id = args[0]
            except Exception:
                pass
            try:
                self.width = args[1]
            except Exception:
                pass
            try:
                self.height = args[2]
            except Exception:
                pass
            try:
                self.x = args[3]
            except Exception:
                pass
            try:
                self.y = args[4]
            except Exception:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ public method """
        return ({"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width})
