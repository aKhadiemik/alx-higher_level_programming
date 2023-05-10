#!/usr/bin/python3
numbers = ["{:02d}".format(n) for n in range(90)]
numbers[-1] += "\n"
print(", ".join(numbers))
