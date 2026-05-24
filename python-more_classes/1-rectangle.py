#!/usr/bin/python3
"""Module that defines a Rectangle class with width and height properties."""


class Rectangle:
    """A class that defines a rectangle by its width and height.

    Private Attributes:
        __width: The width of the rectangle (integer, must be >= 0).
        __height: The height of the rectangle (integer, must be >= 0).
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with width and height validation.

        Args:
            width: The width of the rectangle (default is 0).
            height: The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value: The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value: The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
