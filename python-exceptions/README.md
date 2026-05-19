# Python Exceptions and Error Handling

## Learning Objectives

This project covers the fundamentals of exception handling in Python:

* Why Python programming is awesome
* What's the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What's the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

---

## Why Python Programming is Awesome

Python is awesome because:
- **Simple & Readable**: Code reads like English
- **Versatile**: Works for web, data science, AI, automation
- **Powerful**: Rich standard library with built-in tools
- **Fast to develop**: Write less, do more
- **Exception handling**: Graceful error management without crashing
- **Large community**: Millions of packages and support

---

## Errors vs Exceptions

### Errors
- Serious problems that usually can't be fixed
- Examples: `MemoryError`, `SystemError`, `KeyboardInterrupt`
- **Don't try to catch errors**

### Exceptions
- Abnormal conditions that can be handled
- Examples: `ValueError`, `FileNotFoundError`, `TypeError`
- **Should be caught and handled**

```python
# Errors - don't catch these
MemoryError()
SystemError()
KeyboardInterrupt()

# Exceptions - catch these
ValueError()
TypeError()
FileNotFoundError()
```

---

## What are Exceptions and How to Use Them

An exception is an event that disrupts normal program flow. Python allows you to "handle" it gracefully instead of crashing.

### Common Exceptions

```python
ValueError          # Wrong value
TypeError           # Wrong data type
FileNotFoundError   # File doesn't exist
KeyError            # Dictionary key not found
IndexError          # List index out of range
ZeroDivisionError   # Division by zero
AttributeError      # Attribute doesn't exist
NameError           # Variable not defined
ImportError         # Module not found
```

---

## When Do We Need to Use Exceptions

Use exceptions for **unusual situations** that need special handling:

```python
# ✓ Use exceptions for:

# File I/O
try:
    with open('file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")

# Network operations
try:
    response = requests.get(url, timeout=5)
except requests.ConnectionError:
    print("Network error")

# Data validation
try:
    age = int(user_input)
except ValueError:
    print("Please enter a valid number")

# Database operations
try:
    user = db.get_user(user_id)
except UserNotFoundError:
    print("User not found")
```

### Don't Use Exceptions for Normal Control Flow

```python
# ✗ BAD - using exceptions for normal flow
try:
    value = dictionary[key]
except KeyError:
    value = None

# ✓ GOOD - use normal conditionals
value = dictionary.get(key, None)
```

---

## How to Correctly Handle an Exception

### Basic Try-Except Block

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catch Specific Exceptions

Always catch specific exceptions, not generic ones:

```python
# ✗ BAD - catches everything
try:
    value = int(user_input)
except:
    print("Invalid input")

# ✓ GOOD - catches specific exception
try:
    value = int(user_input)
except ValueError:
    print("Please enter a number")
```

### Multiple Exceptions

```python
try:
    file = open('data.json')
    data = json.load(file)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Access Exception Information

```python
try:
    x = int("invalid")
except ValueError as error:
    print(f"Error: {error}")
    print(f"Type: {type(error).__name__}")
```

---

## What's the Purpose of Catching Exceptions

Catching exceptions allows you to:

1. **Prevent crashes** - Program continues running instead of terminating
2. **Provide friendly messages** - Users see helpful text instead of technical errors
3. **Clean up resources** - Close files, connections, release memory
4. **Log errors** - Record problems for debugging later
5. **Retry operations** - Attempt failed actions again
6. **Recover gracefully** - Use default values or backup options
7. **Maintain data integrity** - Rollback incomplete operations

```python
# Example: prevent crash with friendly message
try:
    items = my_list[index]
except IndexError:
    print(f"Cannot access position {index}")
    items = None
# Program continues instead of crashing
```

---

## How to Raise a Builtin Exception

Use `raise` to deliberately trigger an exception when something is wrong:

```python
# Raise with message
raise ValueError("Age cannot be negative")

# Raise different exception types
raise TypeError("Expected integer, got string")
raise FileNotFoundError("File not found")
raise KeyError("Missing required key")
```

### Raise in Validation Functions

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Usage
try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")
```

### Raise in Your Own Functions

```python
def process_user(user_id):
    if user_id is None:
        raise ValueError("user_id cannot be None")
    if not isinstance(user_id, int):
        raise TypeError("user_id must be an integer")
    # Process the user...
```

---

## When Do We Need a Clean-up Action After an Exception

Use the `finally` block to run cleanup code that **always executes**, whether an exception occurred or not:

### Finally Block

```python
try:
    file = open('data.txt')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # ALWAYS runs
```

### When to Use Finally

Use finally for cleanup:
- **Close files** - Ensure file handles are released
- **Close connections** - Database, network connections
- **Release resources** - Memory, locks, threads
- **Clean up state** - Undo temporary changes

```python
# File handling
file = None
try:
    file = open('data.txt')
    process(file)
except IOError:
    print("Error reading file")
finally:
    if file:
        file.close()

# Database
connection = db.connect()
try:
    connection.execute("UPDATE...")
except Exception:
    connection.rollback()
finally:
    connection.close()
```

### Context Managers (Better Way)

Use `with` statement for automatic cleanup:

```python
# Old way - try/finally
file = open('data.txt')
try:
    content = file.read()
finally:
    file.close()

# Better way - context manager
with open('data.txt') as file:
    content = file.read()
# File automatically closed
```

### Full Try-Except-Finally

```python
def read_file(filename):
    file = None
    try:
        file = open(filename)
        return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    finally:
        if file:
            file.close()
```

---

## Summary

| Concept | Key Points |
|---------|-----------|
| **Errors** | Serious problems - don't catch them |
| **Exceptions** | Recoverable errors - catch and handle them |
| **Try-Except** | Catches exceptions gracefully |
| **Finally** | Always runs cleanup code |
| **Raise** | Trigger exceptions in your code |
| **With** | Automatic resource cleanup (preferred) |

---

## Quick Reference

```python
# Basic try-except
try:
    result = risky_operation()
except ValueError:
    print("Invalid value")

# Multiple exceptions
try:
    something()
except (TypeError, ValueError):
    handle_error()

# With variable
try:
    something()
except Exception as e:
    print(e)

# Finally
try:
    file = open('data.txt')
finally:
    file.close()

# Context manager
with open('data.txt') as f:
    data = f.read()

# Raise exception
if value < 0:
    raise ValueError("Value must be positive")

### Author

Ian Aviles - [GitHub](https://github.com/IanAvi15)
