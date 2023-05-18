#!/usr/bin/python3a
def multiply_by_2(a_dictionary):
    '''
        Create an empty dictionary to store the multiplied values
    '''
    multiplied_dict = {}

    for key, value in a_dictionary.items():
        multiplied_dict[key] = value * 2

    return multiplied_dict
