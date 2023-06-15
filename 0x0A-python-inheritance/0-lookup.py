#!/usr/bin/python3
"""
    Defines a function to list available attributes & methods of object.
"""


def lookup(obj):
    """
    Retrieve a list of attributes from an object that are not callable
    """
    return (dir(obj))
