#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
        Create a set to store unique integers
    '''
    unique_set = set()

    for num in my_list:
        unique_set.add(num)
    total_sum = sum(unique_set)

    return total_sum
