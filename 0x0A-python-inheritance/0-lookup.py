#!/usr/bin/python3
"""
    Return the list of available attributes and methods of an object.
"""


def lookup(obj):
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))
            or attr.startswith("__")]
