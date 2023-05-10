#!/usr/bin/python3
for elem in range(97, 123):
    if elem != 101 and elem != 113:
        print("{:c}".format(elem), end='')
