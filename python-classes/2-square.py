#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """A class that defines a square by its size with validation.

    Private Attributes:
        __size: The size of the square (integer, must be >= 0).
    """

    def __init__(self, size=0):
        """Initialize a Square instance with size validation.

        Args:
            size: The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
