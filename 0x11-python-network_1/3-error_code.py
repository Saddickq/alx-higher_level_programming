#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib
from sys import argv


url = argv[1]
request = urllib.request.Request(url)
try:
    with urllib.request.urlopen(request) as response:
        print(response.read())

except urllib.error.HTTPError as er:
    print(f"Error code: {er.code}")
