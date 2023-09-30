#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


url = argv[1]
data = {'email': argv[2]}
data = urllib.parse.urlencode(data).encode("ascii")

request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode('utf-8'))
