#!/usr/bin/env python3
"""Extending the Python List with Notifications."""


class VerboseList(list):
    """A list subclass that prints a notification on every mutation."""

    def append(self, item):
        """Add item to end of list and notify."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend list with items and notify with count added."""
        items = list(items)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Notify then remove first occurrence of item from list."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Notify then pop item at index (default last) from list."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
