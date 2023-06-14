#!/usr/bin/python3
'''
    Provides fn to return dictionary for corresponding
    JSON object
'''


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representing the JSON serialization of the object.

    """

    return obj.__dict__
