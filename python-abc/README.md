# Python OOP — Abstract Classes, Interfaces & Subclassing

A set of exercises exploring core Object-Oriented Programming concepts in Python: abstract base classes, interfaces, duck typing, method overriding, multiple inheritance, and mixins.

---

## Learning Objectives

- **Abstract Classes** — Define common interfaces while enforcing method implementation in subclasses
- **Interfaces & Duck Typing** — Ensure objects adhere to a specific contract or protocol
- **Subclassing Standard Base Classes** — Extend built-ins like `list`, `dict`, and iterators with custom behavior
- **Method Overriding** — Alter or enhance base class methods in derived classes
- **Multiple Inheritance** — Form complex class relationships using multiple parent classes
- **Mixins** — Compose reusable behavior across unrelated classes

---

## Requirements

- Python 3.x
- No external dependencies

---

**Key concepts:**

- `Animal` inherits from `ABC`, marking it as abstract
- `@abstractmethod` on `sound` forces all subclasses to provide an implementation
- Attempting to instantiate `Animal` directly raises a `TypeError`
- Any subclass that doesn't implement all abstract methods also becomes abstract

---

## How Abstract Classes Work

```
         ┌────────────────────────┐
         │        Animal          │  ← Abstract Base Class (ABC)
         │  @abstractmethod       │
         │  sound() → (no body)   │
         └────────────┬───────────┘
                      │ inherits
          ┌───────────┴───────────┐
          │                       │
   ┌──────▼──────┐         ┌──────▼──────┐
   │     Dog     │         │     Cat     │
   │  sound()    │         │  sound()    │
   │  → "Bark"   │         │  → "Meow"  │
   └─────────────┘         └─────────────┘
```

---

## Resources

- [Python `abc` module documentation](https://docs.python.org/3/library/abc.html)
- [Python 3 Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Real Python — OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [ABC — Abstract Base Classes (docs.python.org)](https://docs.python.org/3/library/abc.html)

---

## Author
- Ian Aviles - [GitHub](https://github.com/IanAvi15)