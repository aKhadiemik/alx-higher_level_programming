#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''Provides Rectangle class that inherits from BaseGeometry'''


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: if the value is not an integer.
        ValueError: if the value is less than 0.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
