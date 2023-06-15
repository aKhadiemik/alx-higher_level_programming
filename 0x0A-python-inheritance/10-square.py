#!/usr/bin/python3
'''Provides Square class, inherits from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square object
    """

    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
        size (int): The size of the square.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
        str: The string representation of the Square object.
        """
        return "[Square] {}/{}".format(
                self._Rectangle__width, self._Rectangle__height)
