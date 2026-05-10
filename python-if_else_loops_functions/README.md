# Python - if/else, loops, functions

## Description
Introduction to Python control flow, loops, and functions. Covers conditional
statements, loops, functions, variable scope, and arithmetic operators.

## Learning Objectives
By the end of this project you should be able to explain:

- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use the `while` and `for` loops
- How to use the `break` and `continue` statements
- How to use `else` clauses on loops
- What does the `pass` statement do, and when to use it
- How to use `range`
- What is a function and how do you use functions
- What does a function return if it has no `return` statement
- Scope of variables
- What's a traceback
- What are the arithmetic operators and how to use them

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable

## Key Concepts

### if/else
```python
a = 12
if a > 2:
    print("greater than 2")
elif a == 2:
    print("equals 2")
else:
    print("less than 2")
```

### while loop
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### for loop with range
```python
for i in range(4):        # 0 1 2 3
    print(i, end=" ")

for i in range(2, 4):     # 2 3
    print(i, end=" ")

for i in range(2, 10, 2): # 2 4 6 8
    print(i, end=" ")
```

### functions
```python
def my_function(x):
    return x * 2
```

### Arithmetic Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `2 + 3 = 5` |
| `-` | Subtraction | `5 - 2 = 3` |
| `*` | Multiplication | `3 * 4 = 12` |
| `/` | Division | `10 / 2 = 5.0` |
| `//` | Floor division | `10 // 3 = 3` |
| `%` | Modulo | `10 % 3 = 1` |
| `**` | Power | `2 ** 3 = 8` |

## Author
- Ian Aviles - [GitHub](https://github.com/IanAvi15)
