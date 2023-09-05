#!/usr/bin/python3
"""
Script accepts URL, sends request to it
 Output: X-Request-Id header variable
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}

    request = requests.post(url, data=values)
    print(request.text)
