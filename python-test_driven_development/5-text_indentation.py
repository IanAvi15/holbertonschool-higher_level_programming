#!/usr/bin/python3
"""Module for text indentation.

This module provides a function to print text with indentation after
specific punctuation characters.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after `.`, `?` and `:`.

    Args:
        text: The text to print (must be a string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        if char in ".?:":
            print(char)
            print()
            # Skip all spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        else:
            print(char, end="")
        i += 1
