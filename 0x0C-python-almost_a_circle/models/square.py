#!/usr/bin/python3
"""
A defined class called square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialisation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str method """
        msg = "[Square] ({}) {}/{} - {}"
        return (msg.format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Getter method for size """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args:
            try:
                self.id = args[0]
            except Exception:
                pass
            try:
                self.size = args[1]
            except Exception:
                pass
            try:
                self.x = args[2]
            except Exception:
                pass
            try:
                self.y = args[3]
            except Exception:
                pass
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """ public method """
        return ({"id": self.id, "x": self.x,
                "size": self.size, "y": self.y})
