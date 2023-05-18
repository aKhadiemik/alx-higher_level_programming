#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        Get the dimensions of the matrix
    '''
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[matrix[i][j] ** 2 for j in range(cols)] for i in range(rows)]

    return result
