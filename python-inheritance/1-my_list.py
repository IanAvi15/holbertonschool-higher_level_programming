#!/usr/bin/python3
"""Module that provides a MyList class that inherits from list."""


class MyList(list):
    """A class that inherits from list with a sorted print method."""

    def print_sorted(self):
        """Print the list sorted in ascending order without modifying it."""
        print(sorted(self))
