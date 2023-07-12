#!/usr/bin/python3
"""
A module that reads and print a file
"""


def read_file(filename=""):
    """ Read a file """

    with open(filename, "r", encoding="utf-8") as my_file:
        data = my_file.read()
        print(data, end="")
