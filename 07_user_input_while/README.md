# 07 - User Input & while Loops

## `input()` — Getting User Input

`input()` in Python is equivalent to `std::getline` in C++ — it reads a full line of input and returns it as `str`. Unlike `std::cin >>` which reads until the first whitespace.

**Applications in Intelligent Systems:** Receiving user commands, reading console configuration, communicating with simple text-based protocols, getting runtime configuration parameters.

### Getting Input and Converting Types

```python
# input() always returns str — like std::getline in C++
name = input("Enter your name: ")
print(f"Hello, {name}!")

# For numbers, manual conversion is required
# C++: int age = std::stoi(input);
age_str = input("Enter your age: ")
age = int(age_str)
print(f"Next year you will be {age + 1}")

# One-liner conversion
height = float(input("Enter your height (m): "))
print(f"Your height is {height} meters")
```

### Comparison with C++

| C++ | Python |
|---|---|
| `std::cin >> x;` (until whitespace) | Not available — `input()` reads full line |
| `std::getline(std::cin, s);` | `s = input()` |
| `std::stoi(s)` | `int(s)` |
| `std::stod(s)` | `float(s)` |

**Key Point:** `input()` always returns `str`. For numbers, manual conversion is required. This is different from `std::cin >> x` which detects the variable type and converts automatically.

---

## The `while` Loop — Review

`while` in Python works exactly like `while` in C++: the loop body executes as long as the condition is true.

```python
# Simple counter — like while in C++
count = 0
while count < 5:
    print(count)
    count += 1

# while with user input — sentinel pattern
message = ""
while message != "quit":
    message = input("Enter a message (or 'quit' to exit): ")
    if message != "quit":
        print(f"You entered: {message}")
```

---

## The `while True` Pattern — Replacing `do-while`

Python does not have `do-while`. The standard and Pythonic pattern for "execute at least once, then check condition" is `while True` with `break`.

```python
# C++ do-while:
# do {
#     x = get_input();
# } while (x < 0);

# Python — while True + break
while True:
    x = int(input("Enter a positive number: "))
    if x > 0:
        break
    print("That's not positive. Try again.")

print(f"You entered: {x}")
```

### Why This Pattern Is Pythonic

There are three ways to simulate do-while:

```python
# Method 1: while True + break — Pythonic (explicit and readable)
while True:
    x = int(input("Number: "))
    if x > 0:
        break

# Method 2: Flag variable — C++-style, unnecessary in Python
first = True
while first or x <= 0:
    first = False
    x = int(input("Number: "))

# Method 3: Repeated code — violates DRY (Don't Repeat Yourself)
x = int(input("Number: "))
while x <= 0:
    x = int(input("Number: "))
```

**Method 1 is more Pythonic because:**
- It explicitly shows the programmer's intent ("loop forever unless break").
- The exit condition is right where the decision is made, not at the top of the loop.
- No code duplication.

---

## Input Validation — The Standard Pattern

Combining `while True` with condition checks is the standard input validation pattern in Python:

```python
# Validating numeric range — standard pattern
while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        break
    print("Out of range. Try again.")

print(f"Valid input: {num}")
```

**Comparison with C++:**

```cpp
// C++ equivalent
int num;
do {
    std::cout << "Enter a number between 1 and 10: ";
    std::cin >> num;
} while (num < 1 || num > 10);
```

In C++, `do-while` does this. In Python, `while True + break` replaces it.

---

## `break` and `continue` — Loop Control

`break` and `continue` in Python work exactly like in C++:

```python
# break — exit loop immediately
for i in range(1, 10):
    if i == 5:
        break       # Exit loop when i == 5
    print(i)        # 1, 2, 3, 4

# continue — skip rest of current iteration
for i in range(1, 6):
    if i == 3:
        continue    # Skip print when i == 3
    print(i)        # 1, 2, 4, 5

# Practical example — sum numbers until 0
total = 0
while True:
    num = int(input("Number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Sum: {total}")
```

---

## Processing Lists with `while` — Common Patterns

### Collecting Items Until Sentinel

```python
# Collecting items — stop at sentinel value
items = []
print("Enter items one by one. Enter 'done' to finish.")

while True:
    item = input("Item: ")
    if item.lower() == "done":
        break
    items.append(item)

print(f"You entered {len(items)} items:")
for i, item in enumerate(items, 1):  # enumerate starting from 1
    print(f"  {i}. {item}")
```

### Removing Elements from a List — Why `for` Is Dangerous

```python
# Safe way — while with condition
numbers = [1, 2, 2, 3, 2, 4]
while 2 in numbers:
    numbers.remove(2)  # One element removed per iteration
print(f"After removing all 2s: {numbers}")  # [1, 3, 4]

# Unsafe way — for loop (elements get skipped!)
numbers = [1, 2, 2, 3, 2, 4]
for n in numbers:
    if n == 2:
        numbers.remove(n)  # DANGER: next element is skipped
print(f"Buggy result: {numbers}")  # [1, 2, 3, 4] — one '2' remains!
```

**Why is `for` dangerous?** When an element is removed, subsequent elements shift one position backward. But the `for` loop's internal counter still moves to the next index. The element that took the removed element's place gets skipped. This bug exists in C++ with `std::vector` and iterators too.

**Pythonic solutions for removing elements:**

```python
numbers = [1, 2, 2, 3, 2, 4]

# Method 1: list comprehension — most Pythonic
filtered = [n for n in numbers if n != 2]

# Method 2: while (safe for one-at-a-time removal)
while 2 in numbers:
    numbers.remove(2)

# Method 3: iterate over a copy
for n in numbers[:]:  # [:] creates a shallow copy
    if n == 2:
        numbers.remove(n)
```

---

## Key Takeaways

1. **`input()` always returns `str`.** Use `int()` or `float()` for numbers.

2. **Python has no `do-while`.** The standard pattern is `while True` + `break`. This is explicit, readable, and free of code duplication.

3. **`while True` + `break` is the primary input validation pattern.** The exit condition is written right where the decision is made.

4. **Never modify a list while iterating with `for`.** Elements shift and some get skipped. Use `while`, list comprehension, or iterate over a copy instead.

5. **For removing elements, list comprehension is the most Pythonic approach.**

6. **`enumerate(items, 1)` starts the index at 1.** Useful for displaying item numbers to users.

---

## Q&A / Key Insights

### Q: Why does removing elements during a `for` loop cause elements to be skipped?
**A:** When an element is removed, later elements shift backward by one position. But the `for` loop's internal counter still advances to the next index. The element that now occupies the removed element's position (the former next element) gets skipped. This bug also exists in C++ with `std::vector` and iterators. The Pythonic solution is list comprehension or `while`.

### Q: Why is `while True` more Pythonic than other do-while alternatives?
**A:** Because it explicitly shows the programmer's intent ("loop forever unless break"), the exit condition is placed right where the decision is made (not at the top of the loop), and it has no code duplication. The flag variable method adds unnecessary state, and the repeated-code method violates the DRY principle.

### Q: Where does `try-except` fit into input validation?
**A:** When input must be converted to a number and the user might enter a string, `try-except ValueError` is used. This topic will be covered in detail in Chapter 10 (Files & Exceptions).