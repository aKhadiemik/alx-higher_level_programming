#!/usr/bin/python3
"""Defines method to find peak in list of unsorted integers"""

def find_peak(list_of_integers):
    """Find peak in list of unsorted integers"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
