#!/usr/bin/python3
'''
    function that divides element by element 2 lists
'''


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                numerator = my_list_1[i]
                denominator = my_list_2[i]
                if isinstance(numerator, (int, float)) and \
                        isinstance(denominator, (int, float)):
                    quotient = numerator / denominator
                else:
                    print("wrong type")
            elif i >= len(my_list_1):
                print("out of range")
            else:
                quotient = 0
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(quotient)
    return result
