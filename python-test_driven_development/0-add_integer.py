#!/usr/bin/python3
"""Module for integer addition operations.

This module provides a function to add two integers or floats,
automatically converting floats to integers before addition.
"""


def add_integer(a, b=98):
    """Adds two integers or floats.

    Args:
        a: First number (integer or float)
        b: Second number (integer or float), defaults to 98

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
