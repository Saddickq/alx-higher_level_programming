#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        size, i = len(my_list) - 1, 0
        while (i <= size):
            print("{:d}".format(my_list[size]))
            size -= 1
