#!/usr/bin/python3
'''Provides fn that writes a string to a text file'''


def write_file(filename="", text=""):
    """
    Write string to text file. Returns number of characters written.

    Args:
        filename (str): name of file to be written.
        text (str): The string to be written to file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
