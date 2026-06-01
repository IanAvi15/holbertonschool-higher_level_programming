#!/usr/bin/env python3
"""The Mystical Dragon - Mastering Mixins."""


class SwimMixin:
    """Mixin that grants swimming ability to any class."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that grants flying ability to any class."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly, composed via mixins."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
