#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == '__main__':
    char = "" if len(argv[1]) == 1 else argv[1]
    data = {'q': char}
    resp = requests.post('http://0.0.0.0:5000/search_user', data)
