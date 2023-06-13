#!/usr/bin/python3
'''Provides fn to append string to end of text file'''


def append_write(filename="", text=""):
    """
        Append string to end of text file, return number of characters added.

        Args:
            filename (str): name of file to which string should be appended.
            text (str): The string to be appended to the file.

        Returns:
            int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added
