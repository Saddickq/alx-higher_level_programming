#!/usr/bin/python3
"""
A module that create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """ Load from json file """
    with open(filename, encoding="utf-8") as my_file:
        obj = my_file.read()
    return (json.loads(obj))
