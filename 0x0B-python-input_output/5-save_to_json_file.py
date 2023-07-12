#!/usr/bin/python3
"""
A module that writes an Object to a text file,
using a JSON representation
"""


import json


with open(filename, "w", encoding="utf-8") as file:
    obj_str = json.dumps(my_obj)
    file.write(obj_str)
