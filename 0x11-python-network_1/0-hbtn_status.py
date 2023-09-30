#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf8')}")
