#!/usr/bin/python3
from models.rectangle import Rectangle
"""
    Provides class that defines Square
"""


class Square(Rectangle):
    """
    Defines a square.

    Args:
    size (int): square side size
    x (int): x coordinate
    y (int): y coordinate
    id (int): id for the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This initializes the Square object.

        Args:
        size (int): Size of the square.
        [optional] x (int): X-coordinate of the square's position.
        Defaults to 0.
        [optional] y (int): Y-coordinate of the square's position.
        Defaults to 0.
        [optional] id (int): Unique identifier for the square.
        Defaults to None.
        """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints string representation of square.

        Returns:
            str: Formatted string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Getter for size.

        Returns:
        int: The size of the Square.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        setter for size

        Args:
        value (int): new value to set

        Raises:
        TypeError: if value is not integer
        ValueError: if value is less than zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        Assign attributes based on no-keyworded and key-worded arguments.

        Args:
        *args: No-keyworded arguments representing the id, size,x,
        and y attributes.
        **kwargs: Key-worded arguments representing the attributes
        to be updated.
        """
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the square.

        Returns:
        dict: Dictionary containing the attributes of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
