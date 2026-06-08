#!/usr/bin/python3
"""Module that provides a function to load an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file to read.

    Returns:
        The Python data structure represented by the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
