#!/usr/bin/python3
"""Module that provides a BaseGeometry class with an area method."""


class BaseGeometry:
    """A base geometry class with an unimplemented area method."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
