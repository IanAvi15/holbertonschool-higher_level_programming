# Python - Everything is Object

## Description
Deep dive into how Python handles data under the hood, covering objects,
classes and instances, mutability, references, aliasing, identity vs.
equality, and how Python passes variables to functions.

## Learning Objectives
By the end of this project you should be able to explain:

- What an object is in Python
- The difference between a class, an object, and an instance
- The difference between immutable and mutable objects
- What a reference is
- What an assignment is
- What an alias is
- How to check if two variables are identical
- How to check if two variables refer to the same object
- How to display a variable's identifier (memory address in CPython)
- What mutability means and why it matters
- The built-in mutable types
- The built-in immutable types
- How Python passes variables to functions

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable
- File length will be tested using `wc`
- `.txt` answer files must contain only one line, no shebang, no leading or
  trailing spaces, and must end with a new line

## Key Concepts

### Objects, Classes, and Instances
```python
class Rectangle:
    """Represent a rectangle."""


my_rectangle = Rectangle()  # my_rectangle is an instance of Rectangle
```

### Identity vs. Equality
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  - same value
print(a is b)   # False - different objects
print(a is c)   # True  - same object (alias)
print(id(a))    # memory address of a
```

### Mutable vs. Immutable
```python
# Mutable - can be changed in place
a_list = [1, 2, 3]
a_list.append(4)   # same object, new content

# Immutable - cannot be changed in place
a_string = "Hello"
a_string += " World"   # creates a NEW object
```

### References and Aliases
```python
a = [1, 2, 3]
b = a          # b is an alias of a - both point to the same object
b.append(4)
print(a)       # [1, 2, 3, 4] - a is affected too
```

### Passing Variables to Functions
```python
def add_item(my_list):
    my_list.append(1)   # mutates the original object


my_list = [1, 2]
add_item(my_list)
print(my_list)   # [1, 2, 1] - passed by object reference
```

## Author
- Ian Aviles - [GitHub](https://github.com/IanAvi15)