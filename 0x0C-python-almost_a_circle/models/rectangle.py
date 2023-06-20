#!/usr/bin/python3
from models.base import Base
"""
    Provides class defining rectangle
"""


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class.

    Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
    x (int): X-coordinate of the rectangle's position.
    y (int): Y-coordinate of the rectangle's position.
    id (int): Unique identifier for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle object.

        Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int, optional): X-coordinate of the rectangle's
        position. Defaults to 0.
        y (int, optional): Y-coordinate of the rectangle's
        position. Defaults to 0.
        id (int, optional): Unique identifier for the rectangle.
        Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets value of width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self__height

    @property
    def x(self):
        """Getter for x co-ord."""
        return self.__x

    @property
    def y(self):
        """Getter for y co-ord."""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width of rectangle."""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height."""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x co-ord."""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y co-ord."""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns area of rectangle."""
        return (self.__height * self.__width)

    def display(self):
        """Prints textual representation of rectangle."""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Displays string representation of rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle using key-worded
        arguments.

        Args:
        *args: No-keyword Arguments for the id, width, height, x,
        and y attributes in the exact order.
        **kwargs: Key-worded arguments representing the attributes
        to be updated.
        """
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
                n += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Return the dictionary representation of the rectangle.

        Returns:
        dict: Dictionary containing the attributes of the rectangle.
        """
        return {
            'y': self.__y,
            'x': self.__x,
            'id': self.id,
            'width': self.__width,
            'height': self.__height
        }
