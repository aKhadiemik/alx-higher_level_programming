#!/usr/bin/python3
'''
    Module contains function to sum 2 ints
'''


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a: The first integer to add.
        b: The second integer to add. Defaults to 98.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
