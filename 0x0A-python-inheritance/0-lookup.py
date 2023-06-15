#!/usr/bin/python3
"""
    Return the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Retrieve a list of attributes from an object that are not callable or
    start with '__'.

    Args:
    obj: An object to perform the attribute lookup on.

    Returns:
    A list of attributes that are not callable or start with '__'.
    """
    return (dir(obj))
