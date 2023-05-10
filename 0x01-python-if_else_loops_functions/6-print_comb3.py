#!/usr/bin/python3
for number in range(0, 89):
    number, end = ((number + 1, '\n') if number == 88 else ((number + 1, ', ')))
    number = (number + 9) if number % 10 == 0 else number
    print("{:02d}".format(number), end=end)
