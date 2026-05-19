### Overview
This project introduces the fundamentals of writing tests in Python. You will learn why testing matters, how to write documentation that generates tests automatically, and how to identify edge cases to make your code more reliable.

### Why Python Programming Is Awesome
Python is awesome because it provides:

Simple, readable syntax

Built‑in tools for testing and documentation

Powerful standard libraries like doctest and unittest

Fast development with fewer bugs thanks to easy test creation

### What Is an Interactive Test?
An interactive test is a test that runs directly from the Python interpreter or command line.
It allows you to:

Try functions manually

Observe behavior in real time

Validate expected outputs quickly

### Why Tests Are Important
Tests help you:

Catch bugs early

Ensure your code behaves as expected

Prevent regressions when updating code

Build confidence in your programs

Document how your functions should work

### Writing Docstrings to Create Tests
Python can generate tests automatically from docstrings using doctest.

A good docstring includes:

A description of the function

Example inputs and outputs

Expected behavior

Example:

python
def add(a, b):
    """
    Returns the sum of two numbers.

    >>> add(2, 3)
    5
    """
    return a + b
Running doctest will verify that the example output is correct.

### Writing Documentation for Modules and Functions
Every module and function should include:

A clear description

Parameters and expected types

Return values

Example usage

Good documentation makes your code easier to understand and test.

### Basic Option Flags for Creating Tests
Common doctest flags include:

-v → verbose mode (shows all tests)

-o → specify options

ELLIPSIS → allows ... in expected output

IGNORE_EXCEPTION_DETAIL → ignores exception text differences

These flags help control how tests run and how strict they are.

### How to Find Edge Cases
Edge cases are unusual or extreme inputs that may break your code.
Examples include:

Empty inputs

Very large values

Wrong data types

Boundary values (e.g., 0, -1, max/min)

Missing arguments

Testing edge cases ensures your code is robust and predictable.

### Author

- Ian Aviles - [GitHub](https://github.com/IanAvi15)
