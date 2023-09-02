#!/usr/bin/python3
"""
Script accepts URL as input, sends request to it
Output is the value of the X-Request-Id header variable
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
