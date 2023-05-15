#!/usr/bin/python3

'''
    print_reversed_list_integer pritns list of integers in reverse
'''


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)-1, -1, -1):
        print("{0:d}".format(my_list[i]))
