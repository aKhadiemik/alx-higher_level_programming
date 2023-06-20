#!/usr/bin/python3
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
""""""


class tests_rectangle(unittest.TestCase):
    """"""
    def test_docstring_exists(self):
        """"""
        self.assertTrue(len(Base.__doc__) >= 1)
