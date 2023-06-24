#!/usr/bin/python3
"""
    Provides a class to serve as the foundation. Other classes
    to inherit from this.
"""


import csv
import json
import os
"""
    Provides a class to serve as the foundation. Other classes
    to inherit from this.
"""


class Base:
    """
    Defines the base class

    Attributes:
    __nb_objects (int): holds number of objects created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization for the base class

        Args:
        id (int): base class id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representaiton of list_dictionaries

        Args:
        list_dictionaries (dict): input list of dictionaries

        Returns:
        str: The JSON string representation of the list of dictionaries.

        Raises:
        TypeError: If list_dictionaries is not a list of dictionaries or None.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(k) == dict for k in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaires")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves JSON string of list_objs to a file

        Args:
        cls: class object.
        list_objs: list of base classes
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns list of JSON strings.

        Args:
        json_string (JSON): json string to parse

        Returns:
        json_string_list: list of JSON strings.
        """
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """
        Returns instance of a class from attributes in dictionary

        Args:
        cls: class object.
        dictionary: holds attribute values.

        Returns:
        dummy: instance of class from attributes in dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.

        Args:
        cls: class object.

        Returns:
        list: A list of instances created from the JSON data.

        Raises:
        FileNotFoundError: If the specified file does not exist.
        """
        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves CSV string of list_objs to file.

        Args:
        cls: class object.
        list_objs: list of base classes
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load objects from a CSV file.

        Returns:
        A list of objects created from the CSV data.

        Raises:
        IOError: If the CSV file cannot be opened or read.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

#    @staticmethod
#    def draw(list_rectangles, list_squares):
#        """
#        Draws list of rectangles, squares.
#
#        Args:
#        list_rectangles: input with list of rectangles.
#        list_squares: input with list of squares.
#        """
#        pass
