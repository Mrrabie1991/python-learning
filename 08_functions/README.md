# 08 - Functions

## Function Definition — Comparison with C++

In Python, functions are defined with the `def` keyword. Unlike C++, parameter types and return types are not mandatory (but can be optionally specified with Type Hints). Any function without an explicit `return` statement returns `None`. `None` is an object of type `NoneType` — unlike `void` in C++ which means "nothing", `None` is an actual value.

**Applications in Intelligent Systems:** Functions are the primary units for organizing program logic — from processing sensor data to executing decision-making algorithms. In intelligent systems, short, single-responsibility functions improve testability and maintainability.

### Definition and Calling

```python
# C++:
# int add(int a, int b) {
#     return a + b;
# }

def add(a, b):
    """Return the sum of a and b."""  # docstring — accessible at runtime
    return a + b

print(add(3, 5))  # 8

# Function without return — returns None
def greet(name):
    """Print a greeting. Returns None implicitly."""
    print(f"Hello, {name}!")

result = greet("Ali")  # "Hello, Ali!"
print(result)          # None
```

### docstring — Runtime-Accessible Documentation

A `docstring` (documentation string) is a multi-line string placed as the first statement inside a function, class, or module. Unlike comments in C++, docstrings are accessible at runtime via `help()` and `.__doc__`.

```python
def add(a, b):
    """Return the sum of a and b.

    This is a docstring — accessible via help(add) or add.__doc__
    """
    return a + b

print(add.__doc__)
help(add)  # Displays the docstring
```

### General Comparison

| C++ | Python |
|---|---|
| `int add(int a, int b) { return a + b; }` | `def add(a, b): return a + b` |
| `void greet(string name) { }` | `def greet(name): ...` (returns None) |
| `/** ... */` — comment, not accessible at runtime | `"""docstring"""` — stored in `__doc__` |
| Return type required | Not required (Dynamic Typing) |
| Parameter types required | Not required (Type Hints optional) |

---

## Parameters and Arguments — Passing to Functions

In Python, everything is passed by **reference** (like `&` in C++). However, behavior depends on whether the object is mutable or immutable. This is exactly the Name Binding model from Chapter 02.

```python
# Immutable parameter — behaves like const & in C++
def increment(x):
    """Rebinds x to a new object — original is untouched."""
    x = x + 1
    return x

num = 5
result = increment(num)
print(f"num: {num}, result: {result}")  # num: 5, result: 6

# Mutable parameter — behaves like & in C++
def append_item(lst, item):
    """Modifies the original object — NOT rebinding."""
    lst.append(item)

numbers = [1, 2, 3]
append_item(numbers, 4)
print(numbers)  # [1, 2, 3, 4] — original changed!
```

**Key Point:** Passing immutable objects (int, str, tuple) to a function behaves like `const &` in C++ — the function cannot modify the original object. Passing mutable objects (list, dict, set) behaves like `&` in C++ — the function can modify the original object's contents.

---

## Scope and Variable Lifetime

In Python, **only functions** create new scopes. Loops, conditionals, and `with` blocks do not create new scopes. This is a fundamental difference from C++.

```python
# Variable defined inside a loop is accessible outside
for i in range(3):
    x = i * 2
print(x)  # 4 — would be an error in C++

while True:
    message = input("Enter: ")
    if message == "quit":
        break
print(message)  # "quit" — variable still alive outside loop
```

Variable lifetime in Python is determined by the **Garbage Collector**, not just by scope end. An object is only removed from memory when **no references** to it remain. If a function returns an object, that object stays alive — even after the function's scope ends.

```python
def create_list():
    x = [1, 2, 3]  # x defined in this scope
    return x        # but the object is returned

result = create_list()  # result points to the list
print(result)           # [1, 2, 3] — list is still alive
```

---

## Default Arguments

Python supports default arguments like C++. However, there is a critical difference: **mutable default arguments are created only once (at function definition)**, not each time the function is called. This is a classic Python pitfall.

```python
# DANGER — mutable default: only created ONCE at function definition
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] — WTF?! Shared list!
print(add_item(3))  # [1, 2, 3]

# Correct way
def add_item_correct(item, lst=None):
    if lst is None:
        lst = []  # Create new list each time
    lst.append(item)
    return lst

print(add_item_correct(1))  # [1]
print(add_item_correct(2))  # [2]
```

**Why does this happen?** Functions in Python are themselves objects. Default arguments are stored in the function's `__defaults__` attribute and are evaluated only once (at `def` time). All calls to the function share the same default object. The standard solution: use `None` as the default and check inside the function.

---

## Keyword Arguments — Passing by Name

Python allows passing arguments by name rather than position. This capability does not exist in C++ (except for designated initializers in C++20, and only for structs).

```python
def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old, lives in {city}")

# Positional (like C++)
describe_person("Ali", 25, "Tehran")

# Keyword — order doesn't matter
describe_person(age=30, name="Sara", city="Isfahan")

# Mixed — positional first, then keyword
describe_person("Reza", city="Shiraz", age=22)
```

**Pythonic Note:** Keyword arguments significantly improve readability, especially for functions with many parameters or boolean parameters whose positional meaning is ambiguous.

---

## `*args` and `**kwargs` — Variable Number of Arguments

Python replaces C++'s `...` (variadic arguments) with `*args` (for positional arguments) and `**kwargs` (for keyword arguments). This mechanism is safer and more flexible than C++.

- `*args` — collects extra positional arguments into a **tuple**.
- `**kwargs` — collects extra keyword arguments into a **dict**.
- The names `args` and `kwargs` are convention — what matters is `*` and `**`.

```python
# *args — variable positional arguments
def sum_all(*args):
    """Return the sum of all arguments. args is a tuple."""
    return sum(args)

print(sum_all(1, 2, 3))       # 6
print(sum_all(1, 2, 3, 4, 5)) # 15

# **kwargs — variable keyword arguments
def print_info(**kwargs):
    """Print all key-value pairs. kwargs is a dict."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ali", age=25, city="Tehran")

# Combining both
def full_signature(required, *args, default="x", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"default: {default}")
    print(f"kwargs: {kwargs}")

full_signature("req", "a", "b", "c", default="y", name="Ali", age=25)
```

---

## Lambda Functions — Anonymous Functions

`lambda` in Python is an anonymous function that can contain **only one expression** (no statements). Unlike C++ where lambdas can have multiple statements, Python's lambda is far more limited. For complex logic, use `def`.

```python
# C++ lambda:
# auto add = [](int a, int b) { return a + b; };

# Python lambda — only one expression
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Common use case — key function for sorting
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Reza", "score": 78},
]
sorted_by_score = sorted(students, key=lambda s: s["score"])

# Lambda in map/filter
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

| Feature | C++ Lambda | Python Lambda |
|---|---|---|
| Body | Multiple statements | Only one expression |
| Capture | Manual with `[=, &x]` | Automatic — everything in scope |
| Storage | `auto` or `std::function` | Regular variable |

**Pythonic Note:** In many cases, list comprehensions or generator expressions are more readable alternatives to `map`/`filter` with lambda.

```python
# More Pythonic approach
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

---

## Type Hints — Optional Type Annotation

Type Hints in Python are **completely optional** and are not checked at runtime (except by static analysis tools like mypy). For functions, using them is Pythonic and recommended. For local variables, they are less common.

```python
from typing import List, Dict, Optional

# Type hints for function — Pythonic and recommended
def calculate_average(scores: list[int]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

# Type hints for variables — optional, less common
x: int = 10
name: str = "Ali"
data: dict[str, int] = {"a": 1, "b": 2}

# Python does NOT enforce types at runtime
x = "Hello"  # Perfectly legal — no error occurs
```

**Recommendation:** Use Type Hints for function signatures (parameters and return type) — they improve readability and maintainability. For internal function variables, they are not necessary.

---

## Memory and Optimization — Additional Notes for C++ Engineers

### Integer Caching

Small integers (typically -5 to 256) are pre-allocated and cached in CPython:

```python
x = 1
y = 1
print(x is y)  # True — both point to the same cached object

a = 1000
b = 1000
print(a is b)  # False — larger numbers create new objects each time
```

### Relative Cost — Mutate vs Rebind

```python
# rebind — new list + (possibly) new objects
x = [1, 2]
x = [3, 4]  # Old list GC'd, new list created

# mutate — same list, only internal pointers change
x = [1, 2]
x[0] = 5    # List stays the same, first pointer rebinds
```

Mutating (modifying in-place) is cheaper than rebinding (creating a new list). However, Python's GC is fast enough for most use cases.

### Using Lists to Simulate "Mutable Variables" Is Not Efficient

```python
# Method 1: direct int — 1 object
x = 5

# Method 2: int in list — 2 objects (list + int)
x = [5]
```

Using a list to simulate a mutable variable does not optimize memory — it increases consumption. The list itself is an extra object with pointer overhead.

---

## Key Takeaways

1. **Functions are defined with `def` and return `None` if there is no `return`.** `None` is an object, not "nothing".

2. **Everything is passed by reference.** Behavior for immutables is like `const &`, for mutables like `&` in C++.

3. **Only functions create new scopes.** Loops, conditionals, and `with` blocks do not.

4. **Variable lifetime is determined by GC, not scope.** An object stays alive as long as there are references to it.

5. **Never use mutable types as default arguments.** Use `None` and check inside the function.

6. **Keyword arguments improve readability and are Pythonic.**

7. **`*args` and `**kwargs` are safer, more flexible replacements for C++'s `...`.**

8. **Python lambda can only contain one expression.** Use `def` for complex logic.

9. **Type Hints are recommended for functions, optional for local variables.** They are not checked at runtime.

10. **Functions in Python are themselves objects.** Default arguments are stored in `__defaults__` and evaluated only once.

11. **Mutating is cheaper than rebinding, but Python's GC is fast enough for most use cases.**

12. **Small integers (-5 to 256) are cached in CPython and are never garbage collected.**

---

## Q&A / Key Insights

### Q: How does variable lifetime work in Python? Does it end with scope like in C++?
**A:** No. Only functions create new scopes. Loops and conditionals do not. Also, object lifetime is determined by the Garbage Collector — an object stays alive as long as there are references to it, even after the function scope ends (e.g., via `return`).

### Q: Why is a variable defined inside a loop accessible outside the loop?
**A:** Because Python does not create a new scope for loops. Only `def`, `class`, and `lambda` create new scopes. This is a fundamental difference from C++.

### Q: Why does `lst=[]` as a default argument cause the list to be shared across calls?
**A:** Functions in Python are objects. Default arguments are created once (at `def` time) and stored in the function's `__defaults__` attribute. Every call that doesn't pass the argument uses the same stored object. Solution: use `None` as the default and create a new list inside the function.

### Q: Does `z[0] = 5` rebind `z` itself or only change the internal pointer?
**A:** Only the internal pointer changes. `z` still points to the same list object (`id(z)` is unchanged). The pointer `z[0]` detaches from the old object and points to the new object (`int(5)`). It's like changing one pointer in an array of pointers.

### Q: Does using a single-element list instead of an immutable variable optimize memory?
**A:** No. The list itself is an extra object with pointer overhead. `x = [5]` creates two objects (list + int), while `x = 5` creates only one. Using a list to simulate a "mutable variable" increases memory consumption, not decreases it.

### Q: Does `x = [1,2]` followed by `x = [3,4]` create three garbage objects?
**A:** The old list is definitely GC'd. However, numbers 1 and 2, if between -5 and 256, are cached in CPython and never GC'd. If the numbers are larger, they too are GC'd. Total: 1 to 3 objects depending on number size.

### Q: Does C++ support keyword arguments?
**A:** No, C++ does not have real keyword arguments like Python. If all parameters have defaults, some can be skipped, but positional order must still be maintained. Writing `f(b=20)` in C++ is an error.

### Q: How is a docstring different from a comment?
**A:** A docstring (between `""" """`) is stored in the object's `__doc__` attribute and is accessible at runtime via `help()`. A comment (`#` or `/** */`) is only for readability and does not exist at runtime. Docstrings are the standard documentation format in Python.