# Python Sets, Dictionaries, and Functional Programming

## Overview

This project covers essential Python data structures and functional programming concepts. By completing this project, you'll master sets, dictionaries, lambda functions, and higher-order functions like `map`, `reduce`, and `filter`.

## Learning Objectives

After completing this project, you will be able to explain:

### Python Programming
- **Why Python programming is awesome** - Understanding Python's elegance, readability, and versatility

### Sets
- **What are sets and how to use them** - Creating and managing unordered collections of unique elements
- **Most common set methods** - Learning methods like `add()`, `remove()`, `discard()`, `union()`, `intersection()`, `difference()`, etc.
- **When to use sets versus lists** - Making appropriate choices based on uniqueness, performance, and use cases
- **How to iterate into a set** - Looping through set elements

### Dictionaries
- **What are dictionaries and how to use them** - Creating and managing key-value pairs
- **When to use dictionaries versus lists or sets** - Choosing the right data structure for lookups and associations
- **What is a key in a dictionary** - Understanding dictionary keys and their properties
- **How to iterate over a dictionary** - Looping through keys, values, or key-value pairs

### Functional Programming
- **What is a lambda function** - Creating anonymous functions for simple operations
- **The `map` function** - Applying a function to every item in an iterable
- **The `reduce` function** - Aggregating values from an iterable into a single result
- **The `filter` function** - Selecting items from an iterable based on a condition

## Key Topics Covered

### 1. Sets

```python
# Creation
my_set = {1, 2, 3, 4, 5}
my_set = set([1, 2, 2, 3])  # Duplicates removed → {1, 2, 3}
empty_set = set()  # Not {} which creates a dict

# Common methods
my_set.add(6)              # Add element
my_set.remove(3)           # Remove (raises error if not found)
my_set.discard(3)          # Remove (no error if not found)
my_set.pop()               # Remove and return arbitrary element
my_set.clear()             # Remove all elements

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.union(set2)           # {1, 2, 3, 4, 5}
set1.intersection(set2)    # {3}
set1.difference(set2)      # {1, 2}
```

### 2. Dictionaries

```python
# Creation
my_dict = {'id': 89, 'name': 'John'}
my_dict = dict(id=89, name='John')

# Accessing values
value = my_dict['id']           # Returns 89 (raises KeyError if not found)
value = my_dict.get('id')       # Returns 89
value = my_dict.get('age', 0)   # Returns 0 (default if not found)

# Common methods
my_dict['age'] = 30             # Add or update
del my_dict['age']              # Delete
my_dict.keys()                  # Get all keys
my_dict.values()                # Get all values
my_dict.items()                 # Get key-value pairs
my_dict.pop('age')              # Remove and return value
my_dict.update({'city': 'NYC'}) # Merge another dict
```

### 3. Iterating Collections

```python
# Iterate over set
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)

# Iterate over dictionary
my_dict = {'id': 89, 'name': 'John'}
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

for value in my_dict.values():
    print(value)
```

### 4. Lambda Functions

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Lambda in sorting
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]
sorted_students = sorted(students, key=lambda x: x[1])
```

### 5. Map Function

```python
# Apply function to every item
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# Using built-in function
lengths = list(map(len, ['hello', 'world', 'python']))
# [5, 5, 6]
```

### 6. Filter Function

```python
# Select items based on condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# Filter out None or empty
values = [1, None, 2, '', 3, 0, 4]
non_empty = list(filter(None, values))
# [1, 2, 3, 4]
```

### 7. Reduce Function

```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
# 15

# Find maximum
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
# 9

# Multiply all
product = reduce(lambda x, y: x * y, numbers)
# 5040
```

## Sets vs Lists

| Feature | Sets | Lists |
|---------|------|-------|
| **Order** | Unordered | Ordered |
| **Duplicates** | Not allowed | Allowed |
| **Indexing** | No | Yes |
| **Mutability** | Mutable | Mutable |
| **Use Case** | Unique items, membership testing | Ordered items, indexing needed |
| **Performance** | O(1) lookup | O(n) lookup |

## Dictionaries vs Lists vs Sets

| Use Case | Best Choice | Why |
|----------|-------------|-----|
| Store unique items | Set | Fast membership testing |
| Store ordered items | List | Need ordering and indexing |
| Key-value associations | Dictionary | Need to look up by key |
| Iterate in order | List or Dictionary | Sets are unordered |
| Check if item exists | Set | O(1) lookup time |

## Project Structure

```
├── README.md                    # This file
├── 0-square_matrix_simple.py    # Matrix operations
├── 1-search_replace.py          # String manipulation
├── 2-uniq_add.py                # Set operations
├── 3-common_elements.py         # Set intersections
├── 4-only_diff_elements.py      # Set differences
├── 5-number_keys.py             # Dictionary operations
├── 6-print_sorted_dictionary.py # Dictionary iteration
├── 7-update_dictionary.py       # Dictionary updates
├── 8-simple_delete.py           # Dictionary deletion
├── 9-multiply_by_2.py           # Map function
├── 10-best_score.py             # Dictionary with max
├── 11-multiply_list_map.py      # Map with lambda
├── 12-roman_to_int.py           # Complex dictionary
└── 100-weight_average.py        # Reduce function
```

## Requirements

- **Python 3.x** - All code should be compatible with Python 3
- **No external imports** - Unless specified in individual tasks
- **Code style** - Follow PEP 8 guidelines
- **Executable scripts** - Add `#!/usr/bin/python3` shebang where applicable
- **Newline at end** - All files should end with a newline

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

- ✅ Understand when to use sets vs lists vs dictionaries
- ✅ Master dictionary access methods (indexing vs `.get()`)
- ✅ Practice iterating over different data structures
- ✅ Use lambda functions for simple, one-time operations
- ✅ Combine `map`, `filter`, and `reduce` for functional programming
- ✅ Remember that sets are unordered but have O(1) lookups
- ✅ Use dictionary comprehensions for efficient dictionary creation

## Common Patterns

### Dictionary Comprehension
```python
# Create dict from keys and values
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Set Comprehension
```python
# Create set from list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
# {1, 2, 3, 4}
```

### Chaining Functions
```python
from functools import reduce

result = reduce(
    lambda x, y: x + y,
    filter(lambda x: x % 2 == 0, 
           map(lambda x: x * 2, range(5)))
)
# Chain: multiply by 2 → filter evens → sum
```

## Additional Resources

- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Dictionaries Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Map, Filter, Reduce](https://docs.python.org/3/library/functions.html#map)
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)

## Author

Ian Aviles (https://github.com/IanAvi15)
