#!/usr/bin/python3
'''
    Module defines a Square class
'''


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Description:
        The `Square` class is used to define a square object.
        private instance attribute '__size' represents size of the square.

    Example:
        >>> my_square = Square(3)
        >>> print(type(my_square))
        <class '__main__.Square'>
        >>> print(my_square.__dict__)
        {}
        >>> print(my_square.size)
        Traceback (most recent call last):
          File "1-main.py", line 9, in <module>
            print(my_square.size)
        AttributeError: 'Square' object has no attribute 'size'
        >>> print(my_square.__size)
        Traceback (most recent call last):
          File "1-main.py", line 13, in <module>
            print(my_square.__size)
        AttributeError: 'Square' object has no attribute '__size'
    """

    def __init__(self, size):
        """
        Initializes a square object with a given size.

        Args:
            size (int): The size of the square.

        Description:
            initializes square object. Sets '__size' attribute to given size.
        """
        self.__size = size
