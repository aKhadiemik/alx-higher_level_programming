#!/usr/bin/python3
"""
Script accepts GitHub credentials, output user ID
from GitHub API
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(r.json().get("id"))
