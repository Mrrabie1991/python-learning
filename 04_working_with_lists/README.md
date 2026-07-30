# 04 - Working with Lists

## The for Loop in Python

### Iterating Over Elements

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

| C++ | Python |
|---|---|
| `for (const auto& item : vec)` | `for item in list:` (read-only) |
| `for (auto& item : vec)` | `for i, item in enumerate(list): list[i] = ...` |

### Modifying List Elements Inside a Loop

In C++, `auto&` allows direct modification. In Python:
- For immutable types (`int`, `str`): use `enumerate` with index assignment.
- For mutable types (`list`): modify the object directly.

```python
# Immutable — requires enumerate
nums = [1, 2, 3]
for i, n in enumerate(nums):
    nums[i] = n * 2
print(nums)  # [2, 4, 6]

# Mutable — direct modification
matrix = [[1, 2], [3, 4]]
for row in matrix:
    row.append(99)
print(matrix)  # [[1, 2, 99], [3, 4, 99]]
```

**Why doesn't `for fruit in fruits: fruit = ...` work?**
Because `fruit` is a name pointing to the object. `fruit = ...` rebinds the name to a new object, rather than modifying the list element.

### enumerate — Iterating with Index

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

| C++ | Python |
|---|---|
| `for (int i=0; i < size; i++)` | `for i, item in enumerate(list):` |

### range — Numeric Loop

```python
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)
```

| C++ | Python |
|---|---|
| `for (int i=0; i<n; i++)` | `for i in range(n):` |
| `for (int i=a; i<b; i+=step)` | `for i in range(a, b, step):` |

---

## List Comprehension

In C++, creating a new vector from an existing one requires a loop. In Python, List Comprehension does it in one line.

### Structure

```python
[expression for item in iterable if condition]
```

### Examples

```python
nums = [1, 2, 3, 4, 5]

# Squares
squares = [n * n for n in nums]
print(squares)  # [1, 4, 9, 16, 25]

# Filter evens
evens = [n for n in nums if n % 2 == 0]
print(evens)  # [2, 4]

# if-else in comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# Calling functions on elements
names = ["ALICE", "BOB"]
lower = [name.lower() for name in names]
print(lower)  # ['alice', 'bob']
```

### Nested Loops in Comprehension

```python
colors = ["red", "blue"]
objects = ["car", "bike"]

# Cartesian product — all combinations
combinations = [f"{c} {o}" for c in colors for o in objects]
print(combinations)  # ['red car', 'red bike', 'blue car', 'blue bike']
```

---

## Tuple — An Immutable List

A `tuple` is like a `list`, but immutable. Roughly equivalent to `const std::vector` or `std::array` in C++.

### Creation and Usage

```python
point = (3, 4)
coordinates = 10, 20  # parentheses optional
single = (42,)        # comma required for single-element tuple

print(point[0])  # 3 — indexing works like list
# point[0] = 5   # Error — tuple is immutable
```

### Unpacking

```python
x, y = point
print(f"x = {x}, y = {y}")  # x = 3, y = 4

# Swap without temporary variable
a, b = 1, 2
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 2, b = 1
```

| C++ | Python |
|---|---|
| `std::tie(x, y) = tuple;` | `x, y = point` |
| `std::swap(a, b);` | `a, b = b, a` |

---

## zip — Pairing Iterables Element-wise

`zip` pairs elements from two (or more) iterables position by position. Returns an iterator of tuples.

```python
colors = ["red", "blue"]
objects = ["car", "bike"]

# zip — positional pairing
pairs = [f"{c} {o}" for c, o in zip(colors, objects)]
print(pairs)  # ['red car', 'blue bike']

# zip with three lists
names = ["Ali", "Sara"]
ages = [25, 30]
cities = ["Tehran", "Isfahan"]
people = [f"{n}, {a}, {c}" for n, a, c in zip(names, ages, cities)]
print(people)  # ['Ali, 25, Tehran', 'Sara, 30, Isfahan']
```

| Goal | Method |
|---|---|
| Cartesian product (all combinations) | `[f"{c} {o}" for c in colors for o in objects]` |
| Positional pairing (one-to-one) | `[f"{c} {o}" for c, o in zip(colors, objects)]` |

> **Note:** `zip` and `enumerate` are iteration tools. Deeper coverage will be provided in Chapter 13 (Advanced Topics).

---

## while Loop and Loop Control

```python
# while
count = 0
while count < 5:
    print(count)
    count += 1

# break — exit loop
for n in range(10):
    if n == 5:
        break

# continue — skip to next iteration
for n in range(5):
    if n == 2:
        continue
    print(n)
```

---

## Q&A / Key Insights

### Q: Why doesn't `for fruit in fruits: fruit = fruit.upper()` modify the list?
**A:** Because `fruit` is a name, not the list element itself. `fruit = ...` rebinds the name to a new object, losing its connection to the list element. For immutable types, use `enumerate` with index assignment. For mutable types, modify the object directly.

### Q: What is the difference between `zip` and nested loops in list comprehension?
**A:** Nested loops produce a Cartesian product (all possible combinations). `zip` pairs elements positionally (first with first, second with second). `zip` uses a single `for` with multiple variables: `for a, b in zip(list1, list2)`.

### Q: Where is `tuple` used?
**A:** For data that should not change — such as coordinates, small records, and dict keys. Also, unpacking and swapping in Python internally use tuples.

### Q: What are `enumerate` and `zip`, and where are they covered in more detail?
**A:** Both are built-in Python functions for working with iterables. Deeper coverage will be provided in Chapter 13 (Advanced Topics).