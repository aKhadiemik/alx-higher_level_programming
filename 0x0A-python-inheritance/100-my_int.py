#!/usr/bin/python3
'''Module provides subclass of int'''


class MyInt(int):
    """
    Subclass of int with overridden equality and inequality operators.
    """
    def __eq__(self, other):
        """
        Override the equality comparison operator (==) for MyInt objects.

        Args:
        other: The object to compare with.

        Returns:
        bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality comparison operator (!=) for MyInt objects.

        Args:
        other: The object to compare with.

        Returns:
        bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
