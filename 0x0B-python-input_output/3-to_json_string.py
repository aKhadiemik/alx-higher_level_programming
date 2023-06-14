#!/usr/bin/python3
'''Provides fn to convert object to JSON representation'''


import json


def to_json_string(my_obj):
    """
        Convert an object to its JSON representation as a string.

        Args:
            my_obj: The object to be converted.

        Returns:
            str: The JSON representation of the object as a string.

    """
    return json.dumps(my_obj)
