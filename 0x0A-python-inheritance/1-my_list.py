#!/usr/bin/python3
"""Provides class that extends built-in list class"""


class MyList(list):
    """
    A custom list class that extends the built-in list class.

    This class provides an additional method, print_sorted(), which
    sorts the list and prints the sorted elements.
    """

    def print_sorted(self):
        """
        Sort list in ascending order and print the sorted elements.
        """
        sorted_list = sorted(self)
        print(sorted_list)
