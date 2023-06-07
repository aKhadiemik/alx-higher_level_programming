#!/usr/bin/python3
import numpy as np
'''
    Module provides fn for matrix multiplication.
'''


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices, returns the resulting matrix.

    Args:
        m_a: The 1st matrix as a list of lists of ints or floats.
        m_b: The 2nd matrix as a list of lists of ints or floats.

    Returns:
        The resulting matrix as a NumPy array.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists,
            or if an element in the matrices is not an integer or float.
        ValueError: If m_a or m_b is empty ([] or [[]]), or if the
            matrices are not rectangular or cannot be multiplied.

    """
    # Convert matrices to NumPy arrays
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    # Perform matrix multiplication using NumPy's dot function
    result = np.dot(np_a, np_b)

    return result.tolist()
