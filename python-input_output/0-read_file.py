#!/usr/bin/python3
"""Module that provides a function to read and print a UTF-8 text file."""


def read_file(filename=""):
    """Read a text file in UTF-8 and print its contents to stdout.

    Args:
        filename (str): Path to the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
