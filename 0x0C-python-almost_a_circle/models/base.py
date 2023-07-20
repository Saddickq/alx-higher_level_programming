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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save list objects into a json file """
        filename = cls.__name__ + ".json"

        if list_objs is None or len(list_objs) == 0:
            json_string = "[]"
        else:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(obj_list)

        with open(filename, mode="w") as my_file:
            my_file.write(json_string)

    def from_json_string(json_string):
        """ json manipulation of data """
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))
