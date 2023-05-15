#!/usr/bin/python3

"""
    fn prints list of integers in reverse
"""


def print_reversed_list_integer(my_list):
    if my_list:
            for i in reversed(my_list):
                print("{0:d}".format(i))
