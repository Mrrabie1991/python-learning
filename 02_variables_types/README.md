# 02 - Variables & Simple Data Types

## Python's Variable Model: Name Binding

In C++, a variable is a box with a fixed size and type (Box Model).
In Python, a variable is a name that points to an object in memory (Name Binding / Sticky Note Model).

### Comparison

| Feature | C++ | Python |
|---|---|---|
| Model | Box Model | Name Binding (Sticky Note) |
| Type | Belongs to the variable | Belongs to the object |
| Memory size | Fixed at compile time | Determined by the object at runtime |
| Type change | Not allowed | Allowed (Dynamic Typing) |
| = operator | Copies value into the box | Rebinds name to a new object |

### Inspection Tools: type() and id()

```python
x = 5
print(type(x))  # <class 'int'> — object type
print(id(x))    # 140735000123456 — memory address (like & in C++)
```

### Example: Rebinding

```python
x = 5           # x points to an int object with value 5
x = "Hello"     # x detaches from int and points to a new str object
x = [1, 2, 3]   # x now points to a list object
```

In C++, an `int` variable cannot hold a string or array. In Python, a name can point to any object.

## Garbage Collection — Fate of Orphaned Objects

When a name detaches from an object and no other name points to it, the object becomes unreferenced.
Python's Garbage Collector (GC) automatically removes such objects from memory at an unspecified time.
Unlike C++, no manual `delete` is needed.

```python
x = 5       # int(5) object created
x = "Hello" # int(5) becomes unreferenced, GC collects it
```

## Simple Data Types

### int — Arbitrary Precision Integer

Unlike C++ where `int` is typically 4 bytes with a fixed range, Python's `int` has unlimited precision.

```python
big = 2 ** 100  # 2^100 — would overflow in C++, fine in Python
print(big)      # 1267650600228229401496703205376
```

### float — Floating Point Number

Python has only one `float` type with 64-bit precision (equivalent to `double` in C++). No separate 32-bit float exists in pure Python.

```python
pi = 3.141592653589793
print(f"Type: {type(pi)}")  # <class 'float'>
```

### str — String

Python `str`:
- Is Unicode by default.
- Is immutable (contents cannot be changed after creation).

```python
s = "Hello Python"
print(s[0])     # H — supports indexing
# s[0] = "h"    # Error — str is immutable
```

### bool — Boolean

`bool` in Python is a subclass of `int` (`True == 1`, `False == 0`).

```python
print(True + True)   # 2
print(bool(0))       # False
print(bool("Hello")) # True
```

### None — The Null Object

`None` is equivalent to `nullptr` in C++. It is a singleton object of type `NoneType`.

```python
x = None
print(x is None)  # True
```

## Type Conversion

```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
int(3.99)       # 3 — truncates, does not round
```

## Immutable vs Mutable

- **Immutable:** `int`, `float`, `str`, `bool`, `NoneType`, `tuple`
- **Mutable:** `list`, `dict`, `set`

Immutability is a property of the object itself, not the name. A name can always be rebound.

```python
s = "Hello"     # str — immutable
s = 5           # rebinding is allowed (name now points to int)
# But s[0] = "h" is not allowed (str contents cannot change)
```

---

## Q&A / Key Insights

### Q: When I write x = 5 and then x = "Hello", what happens to the 5 object?
**A:** The int(5) object becomes unreferenced. Python's Garbage Collector will remove it automatically at an unspecified time. No manual memory management is required.

### Q: Is immutability a property of the name or the object?
**A:** Immutability is a property of the object itself. Names can always be rebound to new objects. Immutability means the object's internal contents cannot be modified.

### Q: Does Python have separate float and double types like C++?
**A:** No. Python has only one float type with 64-bit precision (equivalent to double in C++). External libraries like NumPy provide 32-bit types.

### Q: What is the difference between `is` and `==` in Python?
**A:** `==` compares values (equality). `is` compares object identity — whether two names point to the exact same object.

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True — same values
print(a is b)  # False — different objects
```

### Q: What are `type()` and `id()` used for?
**A:** `type(x)` returns the type of the object. `id(x)` returns the memory address of the object (like the `&` operator in C++). These are essential tools for inspecting and debugging objects in Python.