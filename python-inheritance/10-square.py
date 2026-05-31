#!/usr/bin/python3
"""Module that provides a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class with equal width and height."""

    def __init__(self, size):
        """Initialize a Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
