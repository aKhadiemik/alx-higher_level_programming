#!/usr/bin/python3
import json
'''Provides fn that writes a JSON object to file'''


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file to save the object.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
