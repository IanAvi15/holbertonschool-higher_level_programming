# Python — Input/Output

This project explores file handling and JSON serialization in Python. It covers reading and writing files, managing file state with the `with` statement, and converting between Python data structures and JSON format.

---

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external reference:

**File I/O**
- How to open, read, and write text files in Python
- How to read a file line by line and move the cursor within a file
- How to guarantee a file is properly closed after use
- What the `with` statement is and why it is the preferred approach for file handling

**JSON & Serialization**
- What JSON is and where it is used
- The difference between serialization and deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string back into a Python data structure

**Scripting**
- How to access command-line arguments in a Python script

---

## Requirements

### Python Scripts

| Requirement | Detail |
|---|---|
| Editors | `vi`, `vim`, `emacs` |
| Interpreter | Python 3.8.5 on Ubuntu 20.04 LTS |
| Shebang | `#!/usr/bin/python3` on the first line of every file |
| Style | `pycodestyle` version 2.7.* |
| Executable | All files must be executable |
| Newline | All files must end with a newline |

### Python Test Cases

- All test files must be placed inside a `tests/` directory
- Test files use the `.txt` extension and are written as doctests
- Run the full test suite with:

```bash
python3 -m doctest ./tests/*
```

- Every module, class, and function must include a meaningful docstring — a complete sentence describing its purpose, not just a label
- Docstring presence can be verified with:

```bash
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

---

## AUTHOR

Ian Aviles [GitHub](https://github.com/IanAvi15)