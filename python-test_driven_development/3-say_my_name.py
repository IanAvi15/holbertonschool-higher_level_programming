#!/usr/bin/python3
"""Module for printing names.

This module provides a function to print a person's full name
in a formatted way.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'.

    Args:
        first_name: The person's first name (must be a string)
        last_name: The person's last name (must be a string, default empty)

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
