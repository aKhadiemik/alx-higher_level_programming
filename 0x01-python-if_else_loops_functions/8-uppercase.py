#!/usr/bin/python3
def uppercase(string):
    chars = list(string)
    for i in range(len(chars)):
        if 'a' <= chars[i] <= 'z':
            chars[i] = '{}'.format(chars[i].upper()) 
    print(''.join(chars))
