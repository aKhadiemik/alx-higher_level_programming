#!/usr/bin/python3
def uppercase(string):
    chars = list(string)
    for i in range(len(chars)):
        if 'a' <= chars[i] <= 'z':
            chars[i] = '{}'.format(chr(ord(chars[i]) - 32))
    print(''.join(chars))
