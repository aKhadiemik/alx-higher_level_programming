#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect
"""
"""


class tests_base(unittest.TestCase):
    """"""
    def test_id(self):
        """"""
        base = Base(99)
        self.assertEqual(99, base.id)


class tests_square(unittest.TestCase):
    """"""
    def test_docstring_exists(self):
        """"""
        self.assertTrue(len(Base.__doc__) >= 1)