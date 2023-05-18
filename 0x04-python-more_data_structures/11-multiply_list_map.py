#!/usr/bin/python3a
def multiply_list_map(my_list=[], number=0):
    '''
        Returns new list multiplied by a number using map
    '''
    return list(map(lambda x: x * number, my_list))
