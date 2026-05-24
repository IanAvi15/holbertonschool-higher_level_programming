#!/usr/bin/python3
"""Module that defines a Square class with position."""


class Square:
    """A class that defines a square by its size and position.

    Private Attributes:
        __size: The size of the square (integer, must be >= 0).
        __position: The position of the square (tuple of 2 positive integers).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance with size and position validation.

        Args:
            size: The size of the square (default is 0).
            position: The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            The position of the square as a tuple.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value: The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value) or
                any(isinstance(num, bool) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #.

        If size is 0, prints an empty line.
        Position is used to offset the square with spaces.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
