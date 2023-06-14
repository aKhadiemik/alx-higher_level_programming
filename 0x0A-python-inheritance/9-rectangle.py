#!/usr/bin/python3
'''Module defines a Rectangle class that inherits from BaseGeometry.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle object.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
