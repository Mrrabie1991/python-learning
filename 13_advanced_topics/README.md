# 13 - Advanced Topics

This chapter consolidates concepts referenced throughout Phase 1 that required deeper explanation. Without these concepts, reading professional Python code and major libraries is impossible.

Topics covered: Iterator Protocol, Generator & `yield`, Decorator, Context Manager, Advanced Type Hints, Concurrency (threading/async/multiprocessing), and iteration tools (`zip`, `enumerate`, `map`, `filter`).

---

## Iterator Protocol — The Foundation of All Python Loops

Any object usable in `for x in thing` must follow this protocol:

- `__iter__()` — returns the object itself (or an iterator).
- `__next__()` — returns the next element. Raises `StopIteration` when exhausted.

Behind the scenes, `for` calls exactly these two methods:

```python
numbers = [1, 2, 3]
it = iter(numbers)      # __iter__()
print(next(it))         # __next__() → 1
print(next(it))         # __next__() → 2
print(next(it))         # __next__() → 3
# next(it) → StopIteration
```

**Iterable vs Iterator:**
- **Iterable:** Any object with `__iter__` (list, dict, set, str, range). You can `for` over it.
- **Iterator:** An object with both `__iter__` and `__next__` (like `iter(list)`). Does the actual iteration.

**`range` is a Sequence, not a simple Iterator.** It does not store numbers — it computes them on demand with `start + index * step`. Therefore, `len()` and indexing are O(1), and its memory footprint is constant (a few bytes).

---

## Generator & `yield`

### Problem

Processing large data (10 GB file, infinite stream) without loading everything into memory.

### Solution: `yield`

The `yield` keyword turns a normal function into a **Generator**. A Generator is an Iterator that:

- Resumes from where it paused on each `next()` call (not from the beginning).
- Preserves internal state (local variables) between calls.
- Produces one value at a time — constant memory.

```python
def count_up_to(n):
    """Generate numbers from 1 to n, one at a time."""
    i = 1
    while i <= n:
        yield i    # Return i and pause
        i += 1

g = count_up_to(3)   # generator object — function does NOT execute yet
print(next(g))       # 1 — executes to first yield
print(next(g))       # 2 — resumes from after previous yield
print(next(g))       # 3
# next(g) → StopIteration
```

### `return` vs `yield`

- `return` — function ends. Everything computed at once.
- `yield` — function pauses. Next element computed only on `next()`.

### Why Generators?

For large data, a Generator holds only the current element in memory. In traditional C++, the equivalent is writing a full class with internal state and `operator()()` — Python automates this.

---

## Decorator

### Problem

Adding common behavior (logging, timing, access control) to multiple functions without code duplication.

### Solution: Decorator

A Decorator is a function that takes another function, adds new behavior, and returns a new function.

```python
def measure_time(func):
    """Measure and print execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(1.5)
    return "Done"

# @measure_time means: slow_function = measure_time(slow_function)
```

Decorators used throughout Phase 1: `@property`, `@staticmethod`, `@classmethod`, `@pytest.fixture`, `@pytest.mark.parametrize`.

---

## Context Manager (`with`)

### Problem

Managing resources (file, database, lock) so they are always released — even on error.

### Solution: Context Manager

`with` is syntactic sugar for `try-finally`. Any class with these two methods works with `with`:

- `__enter__` — on entering the `with` block.
- `__exit__` — on exiting (always runs, even on error).

```python
class Timer:
    """Measure execution time of a code block."""
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Elapsed: {time.time() - self.start:.4f}s")
        return False  # Re-raise any exception

with Timer() as t:
    # Code to measure
    sum(range(10_000_000))
```

**C++ comparison:** The equivalent is RAII — constructor/destructor. Key difference: `__exit__` has precise, guaranteed timing, while Python's destructor (`__del__`) has unpredictable timing.

`return False` in `__exit__` means "re-raise the exception" (safe default). `return True` means "suppress the exception" (rare and dangerous).

---

## Advanced Type Hints

Type Hints in Python are **not enforced** — the interpreter completely ignores them. Only static analysis tools (mypy, Pyright) check them.

### Common Types

```python
def process(
    numbers: list[int],
    scores: dict[str, int],
    point: tuple[float, float],
    maybe: int | None,
) -> str:
    ...
```

### Protocol — Formal Duck Typing

```python
from typing import Protocol

class Readable(Protocol):
    def read(self) -> str: ...

def process_data(source: Readable) -> str:
    return source.read()
```

Any class with `read()` is accepted — no common inheritance needed.

### Callable — Functions as Parameters or Returns

```python
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))
```

### TypedDict — Dict with Fixed Structure

```python
from typing import TypedDict

class RobotConfig(TypedDict):
    camera_resolution: tuple[int, int]
    max_speed: int
    sensors: list[str]
```

### Literal — Only Specific Values

```python
from typing import Literal

def set_robot_status(status: Literal["start", "stop", "pause"]) -> str:
    ...
```

---

## Concurrency — Overview

### GIL (Global Interpreter Lock)

CPython has a global lock allowing only one Thread to execute Python code at any moment. This lock switches between Threads every 5 milliseconds.

### I/O-bound vs CPU-bound

- **I/O-bound:** Waiting for network, file, database. GIL is released during waits — Threads work great.
- **CPU-bound:** Heavy computation. GIL is not released — Threads are useless.

### Solutions

| Task | Solution |
|---|---|
| I/O-bound | `asyncio` (modern) or `threading` |
| CPU-bound | `multiprocessing` (separate Python interpreters) |
| I/O + CPU | Combine `asyncio` + `multiprocessing` |

### Async/Await

`async def` creates a coroutine function. `await` means "I'll wait here — event loop, go do other things." Entry point: `asyncio.run(main())`.

```python
async def download_file(file_id: int) -> str:
    await asyncio.sleep(1)
    return f"file_{file_id}.dat"

async def main():
    tasks = [download_file(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    return results

asyncio.run(main())
```

**Rule:** Any function with `await` must be `async def`. Sync functions (pure computation) stay regular; only I/O becomes async.

> **Note:** Concurrency in Python will be explored deeply in later phases (real projects with networking, sensors, robotics). This is conceptual familiarity only.

---

## Iteration Tools: `zip`, `enumerate`, `map`, `filter`

All four return **Iterators** — they produce elements on demand, not build new lists.

### `zip` — Pairing Corresponding Elements

```python
names = ["Ali", "Sara", "Reza"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Building a dict
person = dict(zip(["name", "age"], ["Ali", 25]))

# Matrix transpose
transposed = list(zip(*matrix))
```

### `enumerate` — Index and Value

```python
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
```

### `map` — Apply Function to Each Element

```python
result = map(lambda x: x * x, numbers)  # Iterator
```

**Note:** For lambdas, list comprehension is usually more readable:

```python
result = [x * x for x in numbers]
```

### `filter` — Keep Elements Matching a Condition

```python
result = filter(lambda x: x % 2 == 0, numbers)  # Iterator
# More Pythonic:
evens = [x for x in numbers if x % 2 == 0]
```

### General Rule

- `zip` and `enumerate` — always use them.
- `map` and `filter` with named functions — fine.
- `map` and `filter` with lambdas — prefer list comprehension.

---

## Summary

| Concept | In One Line | C++ Equivalent |
|---|---|---|
| Iterator Protocol | `__iter__` + `__next__` | `begin()`, `end()`, `operator++` |
| Generator | Function with `yield` | C++20 coroutines (`co_yield`) |
| Decorator | Function that takes and returns functions | Higher-order functions / lambda |
| Context Manager | `__enter__` + `__exit__` | RAII (constructor/destructor) |
| GIL | Global lock — one Thread at a time | — (no such limitation) |
| Async | event loop + coroutine | C++20 coroutines |
| `zip` / `map` / `filter` | Iteration iterators | `std::views` (C++20/23) |

---

## Q&A / Key Insights

### Q: Why does `range` use no memory but has `len` and indexing?
**A:** `range` is a Sequence, not a simple Iterator. It computes numbers on demand with `start + index * step`. `len` and indexing are O(1) because they are pure math, not iteration.

### Q: How does `yield` work in a test fixture?
**A:** `yield` turns the function into a Generator. pytest calls `next()` the first time to run setup code (before `yield`), gets the value, runs the test, then calls `next()` again to run cleanup code (after `yield`).

### Q: What do `return False` and `return True` mean in `__exit__`?
**A:** `return False` (default) means "re-raise the exception." `return True` means "suppress the exception" — the program continues. In 99% of cases, `return False` is correct.

### Q: Why was the GIL designed?
**A:** Historical reason — Python's memory management (reference counting) was not thread-safe. The simplest solution was a global lock. It is released during I/O waits but limits CPU-bound work. Solution: `multiprocessing` (separate interpreters).

### Q: What's the difference between Async and Thread?
**A:** Thread = multiple workers, each doing their own thing (with shared GIL). Async = one worker jumping between tasks (event loop). Async has lower overhead and is more modern and Pythonic for I/O-bound work.

### Q: Why are `map` and `filter` with lambda discouraged?
**A:** Because list comprehension is more readable and explicit. `[x * x for x in numbers]` is clearer than `map(lambda x: x * x, numbers)`. For named functions, `map` and `filter` are acceptable.