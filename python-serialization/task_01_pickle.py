#!/usr/bin/python3
"""Module that defines a serializable CustomObject using pickle."""
import pickle


class CustomObject:
    """A custom object that can serialize and deserialize itself via pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.

        Args:
            name (str): The object's name.
            age (int): The object's age.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes to stdout."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Args:
            filename (str): The path to the output file.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a pickle file.

        Args:
            filename (str): The path to the input pickle file.

        Returns:
            CustomObject: The deserialized instance, or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
