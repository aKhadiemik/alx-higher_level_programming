#!/usr/bin/python3a
def only_diff_elements(set_1, set_2):
    '''
        Create empty sets to store elements present in only one set
    '''
    only_set_1 = set()
    only_set_2 = set()

    for element in set_1:
        if element not in set_2:
            only_set_1.add(element)

    for element in set_2:
        if element not in set_1:
            only_set_2.add(element)

    result_set = only_set_1.union(only_set_2)

    return result_set
