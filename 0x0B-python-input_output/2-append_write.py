#!/usr/bin/python3
"""
A module that appends to a fle
"""


def append_write(filename="", text=""):
    """ Append to a file """

    with open(filename, mode="a", encoding="utf-8") as my_file:
        return (my_file.write(text))
