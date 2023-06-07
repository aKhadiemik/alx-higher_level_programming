#!/usr/bin/python3
'''
    Tests for max_integer module
'''


import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function
    """

    def test_max_integer(self):
        """
        Test the max_integer function
        """

        """
        Test with a list containing positive integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        """
        Test with a list containing negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

        """
        Test with a list containing both positive and negative integers
        """
        self.assertEqual(max_integer([-10, 0, 10]), 10)

        """
        Test with an empty list
        """
        self.assertIsNone(max_integer([]))

        """
        Test with a list containing a single integer
        """
        self.assertEqual(max_integer([100]), 100)

        """
        Test with a list containing duplicate integers
        """
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)

        """
        Test with a list containing floating-point numbers
        """
        self.assertEqual(max_integer([1.5, 2.7, 3.9]), 3.9)

if __name__ == '__main__':
    unittest.main()
