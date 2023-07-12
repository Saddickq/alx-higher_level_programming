#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """ Write to file """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        num = my_file.write(text)

    return (num)
