#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    t = response.text
    print("Body response:")
    print(f"\t- type: {type(t)}")
    print(f"\t- content: {t}")
