#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == '__main__':
    char = "" if len(argv) == 1 else argv[1]
    info = {'q': char}
    resp = requests.post('http://0.0.0.0:5000/search_user', data=info)

    try:
        json_data = resp.json()
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except Exception as er:
        print("Not a valid JSON")
