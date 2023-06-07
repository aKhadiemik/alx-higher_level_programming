#!/usr/bin/python3
'''
    Module provides fn that prints text with new lines.
'''


def text_indentation(text):
    """Prints a text with 2 new lines after each \
            occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    result = ""
    newline = "\n" * 2

    for char in text:
        result += char
        if char in punctuation_marks:
            result += newline

    print(result.rstrip())
