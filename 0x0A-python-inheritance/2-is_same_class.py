#!/usr/bin/python3
"""Provides fn that checks whether object belogns to specific class"""


def is_same_class(obj, a_class):
    """
    Check if an object belongs to a specific class.

    Args:
    obj: An object to be checked.
    a_class: A class to compare the object's type with.

    Returns:
    True if the object belongs to the specified class, False otherwise.
    """
    return type(obj) is a_class
