# 05 - if Statements

## Basic if/elif/else Structure

Python uses indentation instead of `{}` to define code blocks.

```python
x = 10

if x > 5:
    print("x is greater than 5")

if x > 20:
    print("x is greater than 20")
else:
    print("x is not greater than 20")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Comparison with C++

| C++ | Python |
|---|---|
| `if (condition) { }` | `if condition:` |
| `else if` | `elif` |
| `else { }` | `else:` |
| `{}` for blocks | `:` + indentation (4 spaces) |
| `switch (x) { }` | `match x:` (Python 3.10+) |

## Indentation

In C++, indentation is for readability and optional. In Python, it is part of the language syntax and mandatory.
Official convention (PEP 8): 4 spaces per indentation level. Do not use tabs.

```python
# Correct
if x > 5:
    print("Hello")
    print("World")

# Error — inconsistent indentation
if x > 5:
    print("Hello")
  print("World")  # IndentationError
```

## Comparison and Logical Operators

### Comparison (same as C++)

```python
5 == 5    # True
5 != 3    # True
5 > 3     # True
5 < 3     # False
5 >= 5    # True
5 <= 3    # False
```

### Logical (keywords instead of && and ||)

```python
a, b = True, False
a and b   # False — equivalent to &&
a or b    # True  — equivalent to ||
not a     # False — equivalent to !
```

### Chained Comparisons

In C++, you write `x > 2 && x < 10`. In Python:

```python
x = 5
2 < x < 10    # True
10 < x < 20   # False
```

| Operator | C++ | Python |
|---|---|---|
| AND | `&&` | `and` |
| OR | `\|\|` | `or` |
| NOT | `!` | `not` |
| Range | `x > 2 && x < 10` | `2 < x < 10` |

## Truthy and Falsy Values

In C++, only `0`, `false`, and `nullptr` are false. In Python, every value has a boolean interpretation.

### Falsy Values (evaluate to False)

```python
bool(0)        # False
bool(0.0)      # False
bool("")       # False — empty string
bool([])       # False — empty list
bool(())       # False — empty tuple
bool({})       # False — empty dict
bool(set())    # False — empty set
bool(None)     # False
```

### Truthy Values (everything else)

```python
bool(1)        # True
bool(-1)       # True
bool("Hello")  # True
bool([1, 2])   # True
bool({"a": 1}) # True
```

### Practical Usage

```python
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")

items = []
if not items:
    print("List is empty")
```

## Ternary Operator — Conditional Expression

```python
x = 10
result = 100 if x > 5 else 200  # C++: (x > 5) ? 100 : 200
status = "pass" if x >= 10 else "fail"
```

| C++ | Python |
|---|---|
| `condition ? true_val : false_val` | `true_val if condition else false_val` |

## match-case — switch Equivalent (Python 3.10+)

```python
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:  # default
        print("Unknown command")
```

### Advanced Pattern Matching

`match-case` goes beyond C++'s `switch` and can destructure objects:

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On y-axis at y={y}")
    case (x, 0):
        print(f"On x-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

Execution flow:
1. `point = (0, 5)` — a tuple with two elements.
2. `case (0, 0):` — both elements 0? No, skip.
3. `case (0, y):` — first element is 0? Yes. Second element bound to variable `y` (`y = 5`). Prints: `On y-axis at y=5`.
4. `match` stops — only the first matching pattern runs.
5. `case (x, y):` is a catch-all (like `default`) and matches anything.

## Assignment Inside Conditions is Forbidden

In C++:
```cpp
if (x = 5) {  // Compiles but buggy — 5 is always true
}
```

In Python:
```python
if x = 5:  # SyntaxError — Python does not allow this
```

Python deliberately forbids this to prevent the classic assignment-in-condition bug.

## x++ and ++x Do Not Exist in Python

`x++` and `++x` are not defined in Python and produce syntax errors. Reason: `int` is immutable, and Python does not support implicit in-place operators for immutable types.

```python
x = 0
x += 1  # Equivalent to x = x + 1 — creates a new object and rebinds
x -= 1
```

Note: `+=` on `int` (immutable) creates a new object. On `list` (mutable), it modifies the object in-place.

## Checking for None with is

Always check for `None` using `is`, not `==`:

```python
x = None
if x is None:      # Correct and Pythonic
    print("x is None")
if x == None:      # Works but not Pythonic
    print("x is None")
```

Reason: `None` is a singleton (only one instance exists). `is` checks identity and is faster and more explicit.

---

## Q&A / Key Insights

### Q: What is `set` ?
**A:** `set` is a collection of unique, unordered elements (like `std::unordered_set` in C++). An empty set is falsy. `set` will be covered in Chapter 06.

### Q: What exactly does `match-case` with pattern matching do?
**A:** `match` compares the value against each `case` pattern in order. The first matching pattern executes, and the rest are ignored. Patterns can include variables that extract (destructure) values. This capability goes well beyond C++'s `switch`.

### Q: Why don't `x++` and `++x` exist in Python?
**A:** Because `int` is immutable in Python and cannot be modified in-place. Python uses `x += 1`, which is equivalent to `x = x + 1` and creates a new object, rebinding the name.