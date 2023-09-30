#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


url = argv[1]
response = requests.get(url)
print(response.headers['X-Request-Id'])
