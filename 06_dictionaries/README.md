# 06 - Dictionaries and Sets

## What is a dict?

A `dict` is a key-value mapping — equivalent to `std::unordered_map` in C++.
The major difference: `dict` is a built-in type in Python, not a library class. Its syntax is far more concise, and working with it is faster than in C++.

**Applications in Intelligent Systems:**
- Storing system configuration
- Mapping sensor IDs to their values
- Structuring input/output data (similar to JSON)
- Counting event frequencies

**Comparison with C++:**

| Feature | C++ (`std::unordered_map`) | Python (`dict`) |
|---|---|---|
| Creation | `std::unordered_map<std::string, int> m = {{"Ali", 25}};` | `d = {"Ali": 25}` |
| Implementation | Hash table | Hash table |
| Access | `m["Ali"]` | `d["Ali"]` |
| Safe access | `m.at("Ali")` — exception if missing | `d.get("Ali")` — None if missing |
| Add/Update | `m["Maryam"] = 28;` | `d["Maryam"] = 28` |
| Remove | `m.erase("Ali");` | `del d["Ali"]` or `d.pop("Ali")` |
| Key check | `m.find("Ali") != m.end()` | `"Ali" in d` |
| Length | `m.size()` | `len(d)` |
| Comprehension | Not available | `{k: v for k, v in ...}` |
| Merge two maps | Manual (loop or merge) | `d1 \| d2` (Python 3.9+) |

### Creating and Accessing Values

```python
# Creating a dict — equivalent to std::unordered_map<std::string, int>
ages = {"Ali": 25, "Sara": 30, "Reza": 22}
empty = {}

# Direct access — raises KeyError if key is missing
print(ages["Ali"])  # 25

# Safe access with get() — returns None or default if key is missing
print(ages.get("Unknown"))        # None
print(ages.get("Unknown", "N/A"))  # 'N/A'
```

**Key Point:** Always use `get()` when a key's existence is uncertain. `d["key"]` raises an error and halts the program. `get()` is safer and more Pythonic.

### Adding, Updating, and Removing

```python
# Adding a new key-value pair
ages["Maryam"] = 28

# Updating an existing value
ages["Ali"] = 26

# Removal with del — raises KeyError if key is missing
del ages["Reza"]

# Removal with pop() — returns the value, or default if key is missing
popped = ages.pop("Sara")          # Returns Sara's value
safe = ages.pop("Unknown", None)   # None — no error
```

**Key Point — `del` vs `pop`:**
- `del d[key]` — removes only, does not return a value. Slightly faster.
- `d.pop(key)` — removes and returns the value. Use when you need the removed value.
- `d.pop(key, default)` — the safest method: returns default if key is missing, no error.

### Checking Key Existence and Length

```python
# Key existence — O(1) average
if "Ali" in ages:
    print("Ali exists")

# Length — number of key-value pairs
print(len(ages))
```

**Key Point:** `in` on a dict checks keys, not values. This is consistent with C++ where `find()` operates on keys.

## Iterating Over dicts

```python
person = {"name": "Ali", "age": 25, "city": "Tehran"}

# Iterate over keys (default)
for key in person:
    print(key)

# Iterate over keys explicitly
for key in person.keys():
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs — most common pattern
for key, value in person.items():
    print(f"{key}: {value}")
```

**Key Point:** `.items()` is the most common way to iterate. `.keys()` and `.values()` return view objects — if the dict changes, these views reflect the changes.

## dict Comprehension

Like list comprehension, dicts can be built in a single line:

```python
# Build dict from a range
squares = {x: x * x for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter with condition
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Reverse keys and values
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

## Merging dicts

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# | operator — Python 3.9+ (d2 values overwrite d1)
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# Older method — unpacking
merged_old = {**d1, **d2}
```

## Valid dict Keys

**Only immutable, hashable types can be dict keys:**
- Allowed: `str`, `int`, `float`, `bool`, `tuple` (if all elements are immutable), `None`
- Not allowed: `list`, `dict`, `set` — because they are mutable and unhashable.

```python
# Valid keys
valid = {42: "int", 3.14: "float", (1, 2): "tuple"}

# Invalid key — error
# invalid = {[1, 2]: "list"}  # TypeError: unhashable type: 'list'
```

**Why this restriction?** dict uses a hash table. To find a key quickly, its hash must be computed. If an object is mutable and changes, its hash changes, and it can no longer be found in the correct hash table bucket.

## dict and JSON

JSON and dict structures are nearly identical. Converting between them is a single line:

```python
import json

# dict -> JSON string
person = {"name": "Ali", "age": 25, "skills": ["Python", "C++"]}
json_string = json.dumps(person, indent=2, ensure_ascii=False)

# JSON string -> dict
parsed = json.loads('{"name": "Sara", "age": 30}')
print(type(parsed))  # <class 'dict'>
```

**Key Point:** `json.dumps()` = **D**ump to **S**tring. `json.loads()` = **L**oad from **S**tring. (For files: `json.dump()` and `json.load()` without the s.)

## set — Unordered Collection of Unique Elements

`set` is like a `dict` but with keys only, no values. Equivalent to `std::unordered_set` in C++.

**Applications:**
- Removing duplicates from a list
- Fast membership testing (O(1))
- Set operations (union, intersection, difference)

```python
# Creating sets — note: {} creates an empty dict, not set
fruits = {"apple", "banana", "cherry"}
empty = set()  # Correct — empty set

# Adding and removing
fruits.add("orange")
fruits.remove("banana")   # KeyError if missing
fruits.discard("mango")   # No error if missing — safer
```

**Key Point — `remove` vs `discard`:**
- `s.remove(x)` — raises `KeyError` if `x` is missing.
- `s.discard(x)` — silently does nothing if `x` is missing. Safer when unsure.

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric difference: {1, 2, 5, 6}
```

**Comparison with C++:**

| Operation | Python | C++ (`std::unordered_set`) |
|---|---|---|
| Create | `{1, 2, 3}` | `std::unordered_set<int> s = {1, 2, 3};` |
| Add | `s.add(4)` | `s.insert(4);` |
| Remove | `s.remove(4)` / `s.discard(4)` | `s.erase(4);` |
| Union | `a \| b` | Requires `std::set_union` |
| Intersection | `a & b` | Requires `std::set_intersection` |
| Membership | `x in s` | `s.find(x) != s.end()` |

---

## Key Takeaways

1. **Always use `get()` for safe access.** Use `d[key]` only when certain the key exists.
2. **Know the difference between `del`, `pop`, and `pop` with default.** Each has its own use case.
3. **Remember the difference between `remove` and `discard` in sets.** `discard` is safer.
4. **dict keys must be immutable.** Because dict uses a hash table internally.
5. **Empty `{}` creates a dict, not a set.** Use `set()` for an empty set.
6. **dict and JSON are nearly identical.** Convert between them with `json.dumps()` and `json.loads()`.
7. **The `|` operator for merging dicts was added in Python 3.9.** Use `{**d1, **d2}` for older versions.

---

## Q&A / Key Insights

### Q: What's the difference between `del`, `remove`, and `discard`?
**A:** `del` is for dicts, removes a key without returning the value. `remove` is for sets, raises an error if the element is missing. `discard` is for sets, silently does nothing if the element is missing.

### Q: Why must dict keys be immutable?
**A:** dict uses a hash table. If a key is mutable and changes, its hash changes, and it can no longer be found in the correct bucket.

### Q: Why doesn't empty `{}` create a set?
**A:** Because `{}` has historically been used for empty dicts. For backward compatibility, empty sets are created with `set()`.

---

**Important — `*` and `**` in Python:**
These operators have nothing to do with pointers or references in C++. They are unpacking operators:
- `*` — unpack an iterable (list, tuple, string)
- `**` — unpack a mapping (dict)

```python
# * — unpack list
numbers = [1, 2, 3]
print(*numbers)  # equivalent to: print(1, 2, 3)

# ** — unpack dict
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}  # {"a": 1, "b": 2}
```

Python has no pointer or reference concepts like C++. Everything is accessed through names pointing to objects (Name Binding model — Chapter 02).
Unpacking is used extensively in function arguments, which will be covered in Chapter 08 (Functions).