#!/usr/bin/python3
'''Provides BaseGeometry class and methods area and
    integer_validator.
'''


class BaseGeometry:
    """
    Represents the base geometry for calculating area
    and validating integer values.
    """
    def area(self):
        """
        Calculates the area of a geometry.

        Raises:
        Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is an integer and greater than 0.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
