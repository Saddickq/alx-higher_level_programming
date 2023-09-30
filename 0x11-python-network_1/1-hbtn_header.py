#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
from sys import argv
import urllib.request


url = argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(response['X-Request-Id'])
