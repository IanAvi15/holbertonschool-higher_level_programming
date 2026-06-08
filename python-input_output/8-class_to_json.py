#!/usr/bin/python3
"""Module that provides a function to convert a class instance to a dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: The __dict__ of the object containing its instance attributes.
    """
    return obj.__dict__
