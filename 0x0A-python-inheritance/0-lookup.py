#!/usr/bin/python3
"""
Return the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Return available attributes and methods
    for a given object

    Parameters
    obj: The given object

    Return
        A list of defined attributes
    """
    return (dir(obj))
