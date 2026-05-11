# Python - Import & Modules

## Description
Introduction to Python modules, imports, and command line arguments.
Covers how to create and use modules, import functions from other files,
and work with command line arguments.

## Learning Objectives
By the end of this project you should be able to explain:

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 22.04 LTS using python3 (version 3.10.*)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable

## Key Concepts

### Importing functions
```python
from my_module import my_function
import my_module
```

### Preventing code from running on import
```python
if __name__ == "__main__":
    # this only runs when the file is executed directly
    # not when it is imported
    my_function()
```

### Using dir()
```python
import my_module
print(dir(my_module))  # lists all names in the module
```

### Command line arguments
```python
import sys
print(sys.argv[0])  # script name
print(sys.argv[1])  # first argument
```

## Author
- Ian Aviles - [GitHub](https://github.com/IanAvi15)
