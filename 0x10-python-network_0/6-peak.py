#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ find peak function """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    number = list_of_integers[0]
    i = 1
    while (i < len(list_of_integers)):
        if (number < list_of_integers[i]):
            number = list_of_integers[i]
        i += 1
    return number
