# 10 - Files & Exceptions

## Reading and Writing Files

File handling in Python is done through the built-in `open()` function and the `with` context manager. `with` guarantees the file will be closed — even if an exception occurs during processing. This is equivalent to RAII in C++.

**Applications in Intelligent Systems:** Reading sensor data from CSV files, storing system configuration in JSON, logging events, and processing large datasets.

```python
# Writing to a file — C++: ofstream file("output.txt"); file << "Hello";
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("This is line 2.\n")

# Reading entire file — C++: string s((istreambuf_iterator<char>(f)), ...);
with open("output.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Reading line by line — C++: getline(file, line)
with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Reading all lines into a list
with open("output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

### Comparison with C++

| Operation | C++ | Python |
|---|---|---|
| Write file | `std::ofstream f("out.txt"); f << "text"; f.close();` | `with open("out.txt", "w") as f: f.write("text")` |
| Read entire file | `std::ifstream f("in.txt"); std::string s(...);` | `content = f.read()` |
| Read line by line | `std::getline(f, line)` | `for line in file:` |
| Close file | `f.close()` (manual or RAII) | Automatic with `with` |

### File Open Modes

| Mode | Description | C++ Equivalent |
|---|---|---|
| `"r"` | Read (file must exist) | `ios::in` |
| `"w"` | Write (creates or overwrites) | `ios::out` |
| `"a"` | Append to end | `ios::app` |
| `"x"` | Exclusive creation — error if exists | — |
| `"rb"` | Read binary | `ios::in \| ios::binary` |
| `"wb"` | Write binary | `ios::out \| ios::binary` |

---

## `with` — Equivalent to RAII in C++

`with` in Python is a context manager that guarantees a resource (file, network, lock) **will** be released, even if an exception occurs. This is exactly the RAII philosophy in C++.

```cpp
// C++ RAII — destructor closes the file
{
    std::ifstream file("data.txt");
    // ... read ...
}  // file automatically closed — even if exception thrown
```

```python
# Python with — context manager
with open("data.txt", "r") as file:
    # ... read ...
    # If an exception occurs here, file is still closed automatically
# file is now closed
```

**Pythonic Principle:** Always use `with` to open files — never use `f = open()` with manual `f.close()`.

---

## Working with CSV and JSON Files

Python has built-in libraries for common data formats. This is a key advantage over C++, which requires external libraries.

### CSV

```python
import csv

# Write CSV
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ali", "25", "Tehran"])

# Read CSV as dictionaries
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']}, lives in {row['City']}")
```

### JSON

```python
import json

# Write JSON
data = {"name": "Ali", "age": 25, "skills": ["Python", "C++"]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Read JSON
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(type(loaded))  # <class 'dict'>
```

---

## Exceptions — Error Handling

### Why Exceptions Instead of Error Codes?

In C-style programming, functions return error codes. This approach has three fundamental problems:

1. **Forgettable checks:** Nothing forces the programmer to check the error code.
2. **Code pollution:** After every call, the error code must be checked — the main logic gets buried under `if` statements.
3. **Error type is unclear:** An error code is just a number — it doesn't say **what error** occurred.

```python
# C-style approach (not Pythonic)
def divide(a, b):
    if b == 0:
        return None  # Error code
    return a / b

result = divide(10, 0)
if result is None:
    print("Error!")
else:
    print(result + 5)  # If you forget to check, error occurs elsewhere
```

```python
# Pythonic approach — EAFP (Easier to Ask Forgiveness than Permission)
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
    print(result + 5)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### EAFP vs LBYL Philosophy

Python has two philosophies for error handling:

- **LBYL — Look Before You Leap:** Check conditions with `if` before acting. C++/Java style.
- **EAFP — Easier to Ask Forgiveness than Permission:** Perform the action, handle errors with `except`. **Pythonic style.**

```python
# LBYL — C-style
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = None

# EAFP — Pythonic
try:
    value = my_dict["key"]
except KeyError:
    value = None
```

**Why is EAFP preferred in Python?**
- In multi-threaded environments, conditions can change between "look" and "leap" (race condition). `try-except` avoids this — the operation and error check are **atomic**.
- Code is more readable — main logic is separated from error handling.
- Uses Python's built-in validators — no need to reinvent the wheel.

### try-except Structure

```python
try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    # If input is not a number
    print("That's not a number!")
except ZeroDivisionError:
    # If number is zero
    print("Cannot divide by zero!")
except Exception as e:
    # Any other error
    print(f"Something else went wrong: {e}")
else:
    # Only if no exception occurred
    print(f"Result: {result}")
finally:
    # Always executed — cleanup
    print("Done.")
```

### try-except Sections

| Section | Description | Required? |
|---|---|---|
| `try:` | Code that may raise an exception | Yes |
| `except ErrorType:` | Handle a specific exception type | At least one |
| `except ErrorType as e:` | Access the exception object | Optional |
| `else:` | If no exception occurred | Optional |
| `finally:` | Always executed — cleanup | Optional |

### Comparison with C++

| C++ | Python |
|---|---|
| `try { } catch (T& e) { }` | `try: ... except T as e:` |
| `std::invalid_argument` | `ValueError` |
| `std::out_of_range` | `IndexError` |
| `std::runtime_error` | `RuntimeError` |
| `throw std::runtime_error("msg");` | `raise RuntimeError("msg")` |

### Common Python Exception Types

| Exception | Cause | Example |
|---|---|---|
| `AttributeError` | Attribute or method doesn't exist | `x = 5; x.append(3)` |
| `IndexError` | Index out of range | `lst = [1,2,3]; lst[10]` |
| `KeyError` | Key doesn't exist in dict | `d = {"a":1}; d["b"]` |
| `TypeError` | Wrong type | `"hello" + 5` |
| `ValueError` | Invalid value | `int("hello")` |
| `FileNotFoundError` | File doesn't exist | `open("x.txt", "r")` |

---

## `raise` — Throwing Exceptions

`raise` creates and throws an Exception object — like `throw` in C++. The object includes an **exception type** (class) and an **error message** (text).

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError(f"Age {age} is unrealistic")
    print(f"Age set to {age}")

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")  # Error: Age 200 is unrealistic
```

**Components of raise:**
- `ValueError` — exception type (inherits from Exception)
- `"Age cannot be negative"` — error message (for display or logging)
- `raise` — throw (like `throw` in C++)

---

## try-except Performance — Myth or Reality?

**Does try-except slow down code?** **No.** On the happy path (no exception), a `try` block has **zero additional overhead** compared to code without `try`. Overhead is only paid when an exception actually occurs — and exceptions should be **rare**.

```python
# try-except is free on the happy path
# Overhead only when an exception actually occurs
# (building stack trace, exception object, and stack unwinding)
```

**Rule:** Don't worry about `try-except` performance. Worry about **readability and correctness**. Exceptions are designed for **exceptional and rare** conditions — not for normal program flow.

---

## Standard Pattern — Combining Files and Exceptions

```python
def read_file_safely(path):
    """Read file contents. Returns content or None on error."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{path}'.")
        return None
    except UnicodeDecodeError:
        try:
            with open(path, "r", encoding="latin-1") as file:
                return file.read()
        except Exception as e:
            print(f"Error: Encoding issue — {e}")
            return None
```

**Note:** Never write bare `except:` — it catches everything, including `KeyboardInterrupt` and `SystemExit`. Always specify the exception type.

---

## Python Exception Hierarchy

```txt
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    └── RuntimeError

```


`except Exception:` catches everything under `Exception` (recommendation: always catch the most specific type).

---

## Key Takeaways

1. **Always use `with` to open files.** Automatic closing even on error — equivalent to RAII in C++.

2. **File modes:** `"r"` (read), `"w"` (write), `"a"` (append), `"rb"`/`"wb"` (binary).

3. **Python has built-in libraries for CSV and JSON.** Unlike C++ which requires external libraries.

4. **EAFP is preferred over LBYL.** "Ask forgiveness, not permission" — perform the action, catch errors with `except`.

5. **`try-except` has zero overhead on the happy path.** Overhead is only paid when an exception actually occurs.

6. **Always specify the exception type in `except`.** Bare `except:` is dangerous — it catches everything.

7. **`raise` throws an Exception object** — like `throw` in C++.

8. **`finally:` is used for cleanup** — always executed, whether an exception occurred or not.

9. **`else:` in try-except runs only if no exception occurred.**

10. **Don't use exceptions for normal program flow.** For example, `try-except` to check "is key in dict?" is not appropriate — use `if`. But for "file must exist" it's perfect — a missing file is truly exceptional.

---

## Q&A / Key Insights

### Q: Does `raise` just throw custom text?
**A:** No. `raise` throws an **Exception object**. The text is just the error message. `raise ValueError("msg")` creates and throws a `ValueError` object with message `"msg"` — equivalent to `throw std::invalid_argument("msg")` in C++.

### Q: Why use try-except when if-else can do the same thing?
**A:** if-else is for **normal, predictable** conditions. try-except is for **exceptional, rare** conditions. try-except makes code more readable (separates normal logic from error handling), errors cannot be ignored, and is safer in multi-threaded environments (the operation and error check are atomic).

### Q: Does try-except slow down execution?
**A:** No. On the happy path (no exception), a `try` block has **zero additional overhead** compared to code without `try`. Overhead is only paid when an exception actually occurs — and exceptions should be rare.

### Q: Why do some C++ projects avoid try-catch?
**A:** Several reasons: 1) In Embedded/Real-time, exceptions are sometimes disabled with `-fno-exceptions`. 2) Some teams use error code patterns or Result types. 3) In C++, exceptions have non-deterministic behavior (stack unwinding). In Python, try-except is standard and Pythonic — low overhead and high readability.

### Q: What do EAFP and LBYL mean?
**A:** LBYL (Look Before You Leap) = check with `if` first, then act (C++ style). EAFP (Easier to Ask Forgiveness than Permission) = act first, catch errors with `except` (Pythonic style). Python prefers EAFP because it's more readable, safer in multi-threaded environments, and compatible with Python's built-in validators.