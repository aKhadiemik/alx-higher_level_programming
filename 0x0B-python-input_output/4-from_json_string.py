#!/usr/bin/python3
'''Provides fn to convert JSON string to corresponding data structure'''
import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.

    """
    return json.loads(my_str)
