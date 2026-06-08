#!/usr/bin/python3
"""Module that provides a function to deserialize a JSON string to an object."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
