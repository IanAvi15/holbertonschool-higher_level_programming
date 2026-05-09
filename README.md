# Python - Hello, World

## Description
Introduction to Python programming, covering the basics of the Python interpreter,
printing text and variables, string manipulation, indexing, slicing, and Python
coding style standards.

## Learning Objectives
By the end of this project you should be able to explain:

- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable

## What is Pycodestyle?
`pycodestyle` is the official standard for Python style code. To check your code:

```bash
pycodestyle your_file.py
```

To install it:
```bash
pip install pycodestyle
```

## Key Concepts

### Print
```python
print("Hello, World")
print(f"{98} Battery street")
```

### Strings and Indexing
```python
a = "Python is cool"
print(a[0])      # P - first character
print(a[-1])     # l - last character
```

### Slicing
```python
a = "Python is cool"
print(a[0:6])    # Python - index 0 to 5
print(a[:6])     # Python - start to index 5
print(a[7:])     # is cool - index 7 to end
print(a[7:-5])   # is - index 7 to -5
```

## Author
- Ian Aviles - [GitHub](https://github.com/IanAvi15)
