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

    result = ""
    for char in text:
        if char in ".?:":
            result += char
            result += "\n\n"
        else:
            result += char

    print(result, end="")
