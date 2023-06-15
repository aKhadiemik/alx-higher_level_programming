#!/usr/bin/python3
'''Module provides add_attribute method'''


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object.

    Args:
    obj: The object to which the attribute will be added.
    attribute: The name of the attribute.
    value: The value to be assigned to the attribute.

    Raises:
    TypeError: If the object does not support dynamic attributes.

    Example:
        >>> obj = SomeClass()
        >>> add_attribute(obj, 'new_attribute', 42)
        >>> print(obj.new_attribute)
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
