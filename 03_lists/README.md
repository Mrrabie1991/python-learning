# 03 - Introducing Lists

## What is a list?

A `list` in Python is equivalent to `std::vector` in C++ — a dynamic array with additional capabilities.

### Comparison with C++

| Feature | std::vector (C++) | list (Python) |
|---|---|---|
| Size | Dynamic | Dynamic |
| Element types | Homogeneous (all same type) | Heterogeneous (mixed types allowed) |
| Syntax | `std::vector<int> v = {1, 2, 3};` | `lst = [1, 2, 3]` |
| Mutable | Yes | Yes — first mutable type on this path |
| Add element | `push_back` | `append` |
| Length | `.size()` | `len(lst)` |
| Membership | `std::find` | `in` |
| Slicing | Not available (requires library) | `lst[start:stop:step]` |
| Memory model | Objects stored contiguously | Pointers stored contiguously |

## Definition and Indexing

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14, True, None]  # Heterogeneous — impossible in std::vector
empty = []

# Indexing (zero-based)
print(numbers[0])    # 1
print(numbers[-1])   # 5 — negative index: last element (no C++ equivalent)
```

## Lists Are Mutable

Unlike `int` and `str` which are immutable, list contents can be changed in place.

```python
numbers = [1, 2, 3]
numbers[0] = 99       # Allowed — list contents are modified
print(numbers)         # [99, 2, 3]

s = "Hello"
# s[0] = "h"           # Error — str is immutable
```

## Key Methods

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")       # Add to end (like push_back)
fruits.insert(1, "mango")     # Insert at position
fruits.remove("banana")       # Remove by value
last = fruits.pop()           # Remove and return last element
print(len(fruits))            # Element count (like .size())
print("apple" in fruits)      # Membership check (like std::find)
```

## Slicing

A capability not available in standard C++. Uses `list[start:stop:step]` syntax.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])      # [2, 3, 4] — start inclusive, stop exclusive
print(numbers[:4])       # [0, 1, 2, 3] — from beginning
print(numbers[6:])       # [6, 7, 8, 9] — to end
print(numbers[::2])      # [0, 2, 4, 6, 8] — every 2nd
print(numbers[::-1])     # [9, 8, 7, ..., 0] — reverse!
```

## Memory Model: Array of Pointers

In C++, `std::vector` stores the actual objects contiguously in heap memory.
In Python, `list` stores an array of pointers, each pointing to an object elsewhere in heap memory.
This design allows elements of different sizes (different types) to be stored together.

## Shallow Copy vs Deep Copy

### Shallow Copy — list.copy()

Copies the list itself, but internal elements still point to the same objects.
Equivalent to copying `std::vector<std::shared_ptr<T>>` — pointers are copied, not the objects they point to.

```python
original = [1, 2, [10, 20]]
shallow = original.copy()

shallow[0] = 99           # Only shallow changes
shallow[2][0] = 999       # original also changes!

print(original)            # [1, 2, [999, 20]]
print(shallow)             # [99, 2, [999, 20]]
print(original[2] is shallow[2])  # True — both point to the same inner list
```

### Deep Copy — copy.deepcopy()

Rebuilds everything from scratch to any depth. New internal objects are created, not just referenced.
In C++, this would require manual `new` for each and every element.

```python
import copy

original = [1, 2, [10, 20]]
deep = copy.deepcopy(original)

deep[0] = 99
deep[2][0] = 999

print(original)            # [1, 2, [10, 20]] — completely untouched
print(deep)                # [99, 2, [999, 20]]
print(original[2] is deep[2])  # False — two completely independent objects
```

### Copy Comparison Table

| Operation | What gets copied | Internal layers | C++ equivalent |
|---|---|---|---|
| `=` | Nothing — just a new name | — | `auto& ref = original;` |
| `list.copy()` | The list + pointers | Shared | Copy vector of shared_ptr |
| `copy.deepcopy()` | The list + all objects to any depth | Fully rebuilt | Manual copy with new for each element |

---

## Q&A / Key Insights

### Q: Why can a Python list hold elements of different types while std::vector cannot?
**A:** A Python list is an array of pointers (each pointer is 8 bytes). All pointers have the same size, so they can be stored contiguously while pointing to objects of completely different sizes. std::vector stores the actual objects contiguously, so all must have the same size.

### Q: When exactly does shallow copy become problematic?
**A:** When a list contains nested mutable objects (like lists inside lists) and only the outer layer is copied. Changes to inner layers affect all copies. For complete independence, use deep copy.

### Q: What is the difference between list.copy() and list[:]?
**A:** Both create a shallow copy with identical results. list.copy() was added in Python 3.3 and is more readable.

### Q: Why does original[2] is shallow[2] return True?
**A:** Because `is` checks object identity (memory address), not value. Shallow copy only copied the list itself, not the inner object. Both names point to the same inner object.