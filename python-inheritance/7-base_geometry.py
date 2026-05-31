#!/usr/bin/python3
"""Module that provides a BaseGeometry class with an integer validator."""


class BaseGeometry:
    """A base geometry class with validation and unimplemented area method."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
