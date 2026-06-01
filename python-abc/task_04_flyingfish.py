#!/usr/bin/env python3
"""The Enigmatic FlyingFish - Exploring Multiple Inheritance."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A flying fish that inherits from both Fish and Bird.

    MRO: FlyingFish -> Fish -> Bird -> object
    """

    def swim(self):
        """Override Fish.swim with flying fish behavior."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override Bird.fly with flying fish behavior."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override both parent habitat methods."""
        print("The flying fish lives both in water and the sky!")
