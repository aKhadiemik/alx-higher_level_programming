#!//bin/python3
"""Provides fn that checks whether object is instance of specified
    class/subclass"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or its subclass.

    Args:
    obj: The object to be checked.
    a_class: The class or a subclass to check against.

    Returns:
    True if the object is an instance of the specified class or its
                                                subclass, False otherwise.
    """
    return isinstance(obj, a_class)
