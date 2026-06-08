#!/usr/bin/python3
"""Module that provides a function to append a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append a string to a text file in UTF-8 and return the character count.

    Args:
        filename (str): Path to the file to append to.
        text (str): Content to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
