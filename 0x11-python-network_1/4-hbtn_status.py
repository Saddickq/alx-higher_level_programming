#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
print(response)
