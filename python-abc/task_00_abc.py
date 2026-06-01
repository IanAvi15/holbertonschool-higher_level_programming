#!/usr/bin/env python3
"""Abstract Animal class and its subclasses using ABC."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that subclasses must implement to return their sound."""
        pass


class Dog(Animal):
    """Concrete subclass of Animal representing a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Concrete subclass of Animal representing a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
