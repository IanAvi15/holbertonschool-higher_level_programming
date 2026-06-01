#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing using ABC."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a generic shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete shape representing a circle."""

    def __init__(self, radius):
        """Initialize circle with a given radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle: π * r²."""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Return the circumference of the circle: 2 * π * |r|."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Concrete shape representing a rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle: width * height."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle: 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any shape-like object (duck typing).

    No isinstance check is used — any object with area() and perimeter()
    methods is accepted as a valid shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
