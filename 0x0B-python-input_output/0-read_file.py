#!/usr/bin/python3
'''Provides function to read a file'''


def read_file(filename=""):
    """
    Read text file, print its content to stdout.

    Args:
        filename (str): name of file to be read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
