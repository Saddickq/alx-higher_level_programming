#!/usr/bin/python3
"""
Load, add and save
"""


from sys import argv
from os.path import isfile


if (__name__ == "__main__"):
    argc = 0
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file
    my_list = []
    filename = "add_item.json"

    argc = len(argv)
    if (isfile(filename)):
        my_list = load(filename)

    if (argc > 1):
        for index in range(1, argc, 1):
            my_list.append(argv[index])

    save(my_list, filename)
