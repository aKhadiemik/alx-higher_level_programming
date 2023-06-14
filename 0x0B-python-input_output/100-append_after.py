#!/usr/bin/python3
'''
    Provides fn that inserts text after each specific line
'''


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a
    specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matching line.

    Returns:
        None

    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
