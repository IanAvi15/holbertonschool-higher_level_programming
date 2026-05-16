# Python Lists and Tuples Learning Project

## Overview

This project covers fundamental Python concepts related to lists, tuples, and sequences. By completing this project, you'll gain a solid understanding of how to work with these essential data structures in Python.

## Learning Objectives

After completing this project, you will be able to explain:

### Lists
- **What are lists and how to use them** - Understanding list creation, indexing, and basic operations
- **Common list methods** - Learning methods like `append()`, `remove()`, `pop()`, `insert()`, `sort()`, `reverse()`, etc.
- **Lists as stacks and queues** - Using lists to implement Last-In-First-Out (LIFO) and First-In-First-Out (FIFO) data structures
- **List comprehensions** - Creating new lists efficiently using concise syntax

### Strings vs Lists
- **Differences and similarities between strings and lists** - Understanding how they're similar as sequences but differ in mutability and purpose
- **Sequences** - Recognizing common properties of sequence types in Python

### Tuples
- **What are tuples and how to use them** - Creating and using immutable sequences
- **When to use tuples versus lists** - Making appropriate choices based on mutability and use cases
- **Tuple packing** - Creating tuples by assigning multiple values
- **Sequence unpacking** - Extracting values from sequences into individual variables

### Advanced Concepts
- **The `del` statement** - How to delete objects, list items, and slices

## Key Topics Covered

### 1. Lists
```python
# Creation
my_list = [1, 2, 3, 4, 5]

# Common methods
my_list.append(6)      # Add element
my_list.remove(3)      # Remove specific element
my_list.pop()          # Remove and return last element
my_list.insert(0, 0)   # Insert at index
my_list.sort()         # Sort in place
my_list.reverse()      # Reverse in place
```

### 2. List Comprehensions
```python
# Concise way to create lists
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

### 3. Tuples
```python
# Immutable sequences
my_tuple = (1, 2, 3, 4, 5)
my_tuple = 1, 2, 3  # Tuple packing (parentheses optional)
```

### 4. Sequence Unpacking
```python
a, b, c = (1, 2, 3)      # Unpacking
x, y = [10, 20]          # Works with lists too
first, *rest = [1, 2, 3] # Extended unpacking
```

### 5. The `del` Statement
```python
my_list = [1, 2, 3, 4, 5]
del my_list[0]      # Delete first element
del my_list[1:3]    # Delete slice
del my_list         # Delete entire list
```

## Project Structure

```
├── README.md                    # This file
├── 0-print_list_integer.py      # Print list integers
├── 1-element_at.py              # Access element at index
├── 2-replace_in_list.py         # Replace element in list
├── 3-print_reversed_list_integer.py  # Print list in reverse
├── 4-new_in_list.py             # Find new elements
├── 5-no_c.py                    # Filter elements
├── 6-print_matrix_integer.py    # Print 2D list
├── 7-add_tuple.py               # Add tuples
├── 8-multiple_returns.py        # Return multiple values
├── 9-max_integer.py             # Find maximum value
├── 10-divisible_by_2.py         # Filter even numbers
├── 11-delete_at.py              # Delete element at index
├── 12-switch.py                 # Swap variables
└── 13-linked_list.py            # Basic linked list
```

## Requirements

- **Python 3.x** - All code should be compatible with Python 3
- **No external imports** - Unless specified in individual tasks
- **Code style** - Follow PEP 8 guidelines
- **Executable scripts** - Add `#!/usr/bin/python3` shebang where applicable

## Getting Started

1. Clone or download this project
2. Review the learning objectives above
3. Complete each task in order
4. Test your code using the provided main files
5. Verify your understanding by explaining each concept

## Testing

Each task typically includes a main file for testing. Run tests with:

```bash
python3 main_file.py
```

## Tips for Success

- ✅ Practice creating and manipulating lists and tuples
- ✅ Understand the mutability differences between lists and tuples
- ✅ Master list comprehensions for efficient code
- ✅ Use tuple unpacking to write cleaner code
- ✅ Know when to use `del` vs other removal methods

## Additional Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Tuples Documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

## Author

Ian Aviles (https://github.com/IanAvi15)
