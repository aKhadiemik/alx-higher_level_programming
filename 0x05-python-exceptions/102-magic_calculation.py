#!/usr/bin/python3
'''
    Perform a magic calculation.

    Args:
        a (int): input parameter.
        b (int): input parameter.

    Returns:
        float: result of magic calculation.


    Raises:
        Exception: If value of 'i' exceeds 'a' in the loop.
'''


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result = a + b
            break
    return result
