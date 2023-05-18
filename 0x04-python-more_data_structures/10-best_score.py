#!/usr/bin/python3a
def best_score(a_dictionary):
    '''
        Check if the dictionary is empty
    '''
    if not a_dictionary:
        return None

    max_score = float("-inf")
    max_key = None

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_key = key

    return max_key
