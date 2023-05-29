#!/usr/bin/python3
import sys
'''
    function that executes a function safel
'''


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
