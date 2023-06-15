#!/usr/bin/python3
''''''


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
        TypeError: If the size is not an integer
        ValueError: If the size is not positive
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
        str: string representation of the square object.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
