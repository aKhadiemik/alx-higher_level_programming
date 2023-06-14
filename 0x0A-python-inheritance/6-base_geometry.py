#!/usr/bin/python3
"""Provides class with area method"""


class BaseGeometry:
    """
    A base class for geometry calculations.

    Methods:
    area: Raises an exception indicating that it is not implemented.
    """
    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
        Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")
