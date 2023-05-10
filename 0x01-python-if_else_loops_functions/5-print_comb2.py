#!/usr/bin/python3
for elem in range(00, 100):
    print("{:02d}".format(elem), end=("\n", ", ")[elem != 99])
