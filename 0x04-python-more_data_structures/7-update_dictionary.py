#!/usr/bin/python3a
def update_dictionary(a_dictionary, key, value):
    '''
        Update the value if the key already exists in the dictionary
    '''
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
