#!/usr/bin/python3
numbers = [f"{n:02d}" for n in range(90)]
numbers[-1] += "\n"
print(", ".join(numbers))
