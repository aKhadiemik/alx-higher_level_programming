#!/usr/bin/python3
from models.base import Base
"""
    Provides class defining rectangle
"""

class Rectangle(Base):
    """
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets value of width"""
        return self.__width

    @property
    def height(self):
        """"""
        return self__height

    @property
    def x(self):
        """"""
        return self.__x

    @property
    def y(self):
        """"""
        return self.__y

    @width.setter
    def width(self, value):
        """"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """"""
        return (self.__height * self.__width)

    def display(self):
        """"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """"""
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
        """"""
        return {
            'y': self.__y,
            'x': self.__x,
            'id': self.id,
            'width': self.__width,
            'height': self.__height
        }

        
