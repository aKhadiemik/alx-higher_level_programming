#!/usr/bin/python3
"""Provides fn that checks for inheritance"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specific class.

    Args:
    obj: The object to be checked.
    a_class: The class to check against.

    Returns:
    A boolean value indicating whether the object inherits from the class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
