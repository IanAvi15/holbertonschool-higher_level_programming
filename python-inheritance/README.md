# Python Inheritance

## Superclass, Base Class, or Parent Class

A superclass is the class being inherited from. It defines attributes and methods that can be shared with other classes.

```python
class Animal:
    def speak(self):
        print("Some sound")
```

---

## Subclass

A subclass inherits from another class. It gains all the attributes and methods of the parent and can extend or override them.

```python
class Dog(Animal):
    def speak(self):
        print("Woof")
```

---

## Listing All Attributes and Methods

Use the built-in `dir()` function to list all attributes and methods of a class or instance.

```python
print(dir(Dog))
print(dir(Dog()))
```

---

## When Can an Instance Have New Attributes

An instance can receive new attributes at any time after creation by assigning directly to it.

```python
dog = Dog()
dog.name = "Rex"
```

---

## How to Inherit a Class from Another

Place the parent class name in parentheses when defining the child class.

```python
class Cat(Animal):
    pass
```

---

## Multiple Base Classes

Python supports multiple inheritance. List all parent classes separated by commas.

```python
class C(A, B):
    pass
```

---

## The Default Class Every Class Inherits From

In Python 3, every class implicitly inherits from `object` if no other parent is specified. It provides default implementations of methods like `__str__`, `__repr__`, and `__eq__`.

```python
class MyClass:
    pass
# same as
class MyClass(object):
    pass
```

---

## Overriding a Method or Attribute

Define a method or attribute in the subclass with the same name as the one in the parent.

```python
class Dog(Animal):
    def speak(self):  # overrides Animal.speak
        print("Woof")
```

---

## What Is Available to Subclasses by Inheritance

A subclass has access to all public and protected attributes and methods of the parent. Private attributes (prefixed with `__`) are name-mangled and not directly accessible.

---

## Purpose of Inheritance

Inheritance promotes code reuse and logical organization. Subclasses extend a parent class instead of rewriting shared logic, keeping code DRY (Don't Repeat Yourself).

---

## Built-in Functions: isinstance, issubclass, type, super

### `isinstance(obj, cls)`
Returns `True` if `obj` is an instance of `cls` or any subclass of it.
```python
isinstance(dog, Dog)     # True
isinstance(dog, Animal)  # True
```

### `issubclass(cls, parent)`
Returns `True` if `cls` is a subclass of `parent`.
```python
issubclass(Dog, Animal)  # True
issubclass(Dog, Dog)     # True
```

### `type(obj)`
Returns the exact type of an object. Does not consider inheritance.
```python
type(dog) is Dog     # True
type(dog) is Animal  # False
```

### `super()`
Refers to the parent class, allowing you to call its methods from the subclass.
```python
class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

## Author
- Ian Aviles - [GitHub](https://github.com/IanAvi15)