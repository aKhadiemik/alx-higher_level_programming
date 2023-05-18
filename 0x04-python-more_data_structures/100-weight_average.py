#!/usr/bin/python3a
def weight_average(my_list=[]):
    '''
        Calculates the weighted avg of list of int tuples
    '''
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
