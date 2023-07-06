#!/usr/bin/python3

"""
A module that introduces the user with
their first and last name
"""


def say_my_name(first_name, last_name=""):
    """A function that prints the full name of a person
    Args:

    first_name(str): the first name of user
    last_name(str): the lastname of user(optional)

    raise: TypeError if args is not string
    print: first_name and last_name together
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
