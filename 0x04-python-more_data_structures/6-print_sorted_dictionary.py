#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dict in sorted(a_dictionary):
        print("{}: {}".format(dict, a_dictionary[dict]))
