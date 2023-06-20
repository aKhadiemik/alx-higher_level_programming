#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect
"""
Base module test cases.
"""


class TestsBase_cases(unittest.TestCase):
    """
    Defines test cases.
    """

    def test_no_id(self):
        """
        No id.
        """
        base = Base()
        self.assertEqual(99, base.id)

    def test_id(self):
        """
        Valid id.
        """
        base = Base(99)
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
