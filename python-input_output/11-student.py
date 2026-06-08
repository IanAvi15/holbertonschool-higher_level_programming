#!/usr/bin/python3
"""Module that defines a Student class with serialization and reload support."""


class Student:
    """Represent a student with save and restore functionality."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to include.
                          If None or not a list, all attributes are returned.

        Returns:
            dict: The filtered or full attribute dictionary.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all instance attributes with values from a dictionary.

        Args:
            json (dict): A dictionary mapping attribute names to their values.
        """
        for k, v in json.items():
            setattr(self, k, v)
