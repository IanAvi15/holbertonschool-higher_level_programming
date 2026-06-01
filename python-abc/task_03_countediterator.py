#!/usr/bin/env python3
"""CountedIterator - Keeping Track of Iteration."""


class CountedIterator:
    """An iterator wrapper that counts how many items have been fetched."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to zero."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items fetched so far."""
        return self.count

    def __next__(self):
        """Fetch the next item, increment counter, or raise StopIteration."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return self to make CountedIterator usable in for-loops."""
        return self
