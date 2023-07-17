#!/usr/bin/python3
"""
A defined called Base
"""


import json


class Base:
    """ Public class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json manipulation of data """
        size = len(list_dictionaries)
        if list_dictionaries == None or size <= 0:
            return ("[]")
        return (json.dumps(list_dictionaries))
