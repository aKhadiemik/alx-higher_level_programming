#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect
"""
Base module test cases.
"""


class tests_base(unittest.TestCase):
    """
    Defines test cases.
    """
    def test_id(self):
        """
        Valid id.
        """
        base = Base(99)
        self.assertEqual(99, base.id)

    def test_no_id(self):
        """
        No id.
        """
        base = Base()
        self.assertEqual(99, base.id)

    def test_neg_id(self):
        """
        Negative id.
        """
        base = Base(-99)
        self.assertEqual(-99, base.id)

    def test_zero_id(self):
        """
        Zero as id.
        """
        base = Base(0)
        self.assertEqual(0, base.id)

class tests_square(unittest.TestCase):
    """"""
    def test_docstring_exists(self):
        """"""
        self.assertTrue(len(Base.__doc__) >= 1)
