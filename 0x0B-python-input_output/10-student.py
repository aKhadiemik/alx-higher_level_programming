#!/usr/bin/python3
'''
    Provides a student class and methods that operate on it
'''


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a student instance with first_name, last_name, and age.

        Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
        attrs (list): List of attribute names to retrieve (default: None).

        Returns:
        dict: A dictionary representing the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr, None)
                    for attr in attrs if hasattr(self, attr)}
