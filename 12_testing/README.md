# 12 - Testing Your Code

## Why Test?

You write a function like `divide(a, b)`. You use it in 10 different places. Everything works.

Six months later, someone (or you) changes that function. How do you know the change didn't break those 10 other places?

**If you have tests:** Run `pytest`. The test fails. You catch the bug before it reaches the user.

**If you don't have tests:** Ten days later, a user reports "the output is wrong." You don't know where the problem is.

A test is just another function that calls your main function with various inputs and checks that the output matches what you expect.

## Unit Test vs Integration Test

### Unit Test

**Definition:** Testing **a single function or class** in isolation, with no dependencies on files, network, or databases.

**Goal:** If it fails, you know exactly which function has the problem.

**Characteristics:** Fast (milliseconds), many (hundreds), run every time you change the code.

### Integration Test

**Definition:** Testing **multiple modules working together** — e.g., Camera + PathPlanner + Controller.

**Goal:** Ensuring that modules work correctly when connected.

**Characteristics:** Slower (may need files or network), few, run before commit or in CI/CD.

### Comparison

| | Unit Test | Integration Test |
|---|---|---|
| What it tests | One function/class | Multiple modules together |
| Speed | Very fast | Slower |
| Count | Many | Few |
| Error location | Exact | Unknown module |
| Tool | pytest | pytest (same tool) |
| Dependencies | None | May need file/database/network |

---

## pytest from Scratch

### What is pytest?

A **testing framework** for Python. A framework gives you rules and tools to write and run your tests.

**Comparison with C++:**
- C++: Google Test (gtest) — compile, build executable, register tests.
- Python: pytest — write a `.py` file and run `pytest`.

### How pytest Discovers Tests

pytest automatically finds test files and functions by **naming convention**:

- **Test files:** Must start with `test_` or end with `_test`.
- **Test functions:** Must start with `test_`.
- **Test classes:** Must start with `Test`.

No registration needed. pytest finds everything automatically.

### First Test

```python
# calculator.py — code to test

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_calculator.py — tests

from calculator import add, divide
import pytest

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5       # If False, test fails
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Test that divide raises ValueError on zero division."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

```bash
pytest
# Output: 3 passed in 0.03s
# . = pass, F = fail, E = unexpected error
```

### What is assert?

A Python statement that checks a condition. If `True`, nothing happens. If `False`, it raises `AssertionError` and the test fails.

```python
assert add(2, 3) == 5   # True → test continues
assert add(2, 3) == 10  # False → test fails
```

**C++ comparison:**
- C++: `EXPECT_EQ(add(2, 3), 5);` — gtest macro
- Python: `assert add(2, 3) == 5` — built-in Python keyword

### What is pytest.raises?

Use it when you want to test that a function **must** raise an exception.

```python
def test_divide_by_zero():
    with pytest.raises(ValueError):     # I expect ValueError
        divide(10, 0)                   # This line should raise

    # If no exception → test fails
    # If wrong exception → test fails
    # If ValueError → test passes
```

---

## Fixture — Shared Data for Tests

### Problem: Duplicate Code in Tests

If class `Robot` needs a `Camera` for testing, without fixtures you must manually create a Camera in every test — repeated code.

### Solution: Fixture

A fixture is a helper function that creates **the data or object you need** once, and pytest passes it to your tests automatically.

```python
import pytest

@pytest.fixture
def robot():
    """Create a Robot ready for testing."""
    cam = Camera(resolution=(1920, 1080))
    return Robot(cam)

# Tests receive robot as a parameter
def test_robot_move(robot):
    assert robot.move() == "Moving"

def test_robot_stop(robot):
    assert robot.stop() == "Stopped"
```

### How pytest Injects Fixtures

1. pytest sees that `test_robot_move` has a parameter named `robot`.
2. It searches for a fixture named `robot`.
3. It finds `@pytest.fixture` on the `robot()` function.
4. It **calls** the `robot()` function.
5. It takes the return value (a Robot object).
6. It passes that value as the `robot` argument to the test.

**This mechanism is called Dependency Injection.** pytest finds fixtures by **parameter name**. That's why the name must match exactly.

### yield in Fixture — Setup and Cleanup

`yield` allows a fixture to do work **before the test** (setup) and **after the test** (cleanup). Code before `yield` is setup. Code after `yield` is cleanup.

**Note:** `yield` is part of Generators, covered in depth in Chapter 13 (Advanced Topics). Here, just see its use in fixtures.

```python
@pytest.fixture
def database():
    # Setup — runs before the test
    db = Database("test_config.json")
    db.connect()
    
    yield db  # ← Test runs here. db is passed to the test.
    
    # Cleanup — runs after the test
    db.disconnect()
    db.delete_all()
```

### Fixture Scope — How Often to Create

| Scope | Created | Use Case |
|---|---|---|
| `function` | Once per test (default) | Isolated data |
| `class` | Once per test class | Shared data within a class |
| `module` | Once per test file | Shared settings |
| `session` | Once per test session | Database, network |

```python
@pytest.fixture(scope="function")   # default
def fresh_list():
    return []

@pytest.fixture(scope="module")     # one instance for all tests in this file
def shared_config():
    return {"timeout": 10}
```

---

## Parametrize — One Test, Many Inputs

When you have multiple tests that only differ in their inputs, use `parametrize` instead of writing duplicate tests.

```python
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),        # a=2, b=3, expected=5
    (-2, -3, -5),     # a=-2, b=-3, expected=-5
    (0, 5, 5),        # a=0, b=5, expected=5
    (100, 200, 300),  # a=100, b=200, expected=300
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

This test runs **4 times** — once per tuple. `@pytest.mark.parametrize` must come **immediately before** the test function, because it's a decorator and Python's decorator rules require this.

```python
# Testing exceptions with parametrize
@pytest.mark.parametrize("a, b", [
    (10, 0),
    (0, 0),
    (-5, 0),
])
def test_divide_by_zero(a, b):
    """For all inputs, divide should raise ValueError."""
    with pytest.raises(ValueError):
        divide(a, b)
```

---

## Markers — Tags on Tests

Markers are tags you attach to tests. They have three main uses:

### 1. Grouping Tests

Some tests are fast (run every minute). Some are slow (run only before commit).

```python
@pytest.mark.slow
def test_heavy_computation():
    result = sum(range(10_000_000))
    assert result > 0

@pytest.mark.fast
def test_quick_check():
    assert 1 + 1 == 2
```

```bash
pytest -m fast           # Only fast
pytest -m "not slow"     # All except slow
```

### 2. Skipping Tests

When a test is not ready, or only works on a specific platform.

```python
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
def test_linux_feature():
    pass
```

### 3. Expected Failure

When you know a bug exists and plan to fix it later. The test runs — if it fails, it shows yellow (warning, expected). If it passes, it shows green (XPASS — the bug is probably fixed).

```python
@pytest.mark.xfail(reason="Known bug #1234")
def test_known_bug():
    assert 1 + 1 == 3  # We know this fails
```

---

## Coverage — Test Coverage

A metric showing **what percentage of your code lines are tested.**

```bash
pip install pytest-cov
pytest --cov=calculator
# Output: calculator.py  12 lines   83% covered
```

Low coverage means there are code sections with no tests. If someone changes those sections, tests won't fail — but bugs will enter the system.

In CI/CD, a threshold is usually set:

```bash
pytest --cov=my_package --cov-fail-under=80
# CI fails if coverage is below 80%
```

---

## Additional Topics

### conftest.py — Shared Fixtures

Place fixtures used by multiple test files in `conftest.py`. pytest automatically discovers them — no import needed.

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Ali", "age": 25}
```

```python
# tests/test_calculator.py
def test_with_data(sample_data):   # No import — auto-discovered
    assert sample_data["name"] == "Ali"
```

### tmp_path — Temporary File for Testing

When a test needs a file, use `tmp_path` (built-in pytest fixture). The file is automatically deleted after the test.

```python
def test_write_file(tmp_path):
    file = tmp_path / "test_output.txt"
    file.write_text("Hello, pytest!")
    assert file.read_text() == "Hello, pytest!"
```

### monkeypatch — Replacing Functions

When a function depends on external things (time, network, user input), use `monkeypatch` to replace them.

```python
def test_get_greeting_morning(monkeypatch):
    class MockDateTime:
        @staticmethod
        def now():
            return datetime(2026, 1, 1, 9, 0, 0)
    
    monkeypatch.setattr("datetime.datetime", MockDateTime)
    assert get_greeting() == "Good morning"
```

### capsys — Testing print Output

To test what a function prints.

```python
def test_greet_output(capsys):
    greet("Ali")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Ali!\n"
```

### Arrange-Act-Assert (AAA) — Test Writing Pattern

Every good test has three sections:

```python
def test_withdraw():
    # Arrange: set up data
    account = BankAccount(balance=100)
    
    # Act: do the thing you're testing
    result = account.withdraw(30)
    
    # Assert: check the result is what you expected
    assert result == 70
    assert account.balance == 70
```

---

## Comparison with C++ (Google Test)

| C++ (gtest) | Python (pytest) |
|---|---|
| `TEST(Suite, Name) { }` | `def test_name():` |
| `EXPECT_EQ(a, b);` | `assert a == b` |
| `SetUp()` / `TearDown()` | Fixture with `yield` |
| `TEST_P` + `INSTANTIATE_TEST_SUITE_P` | `@pytest.mark.parametrize` |
| `GTEST_SKIP()` | `@pytest.mark.skip` |
| Must compile, build executable | `pytest` |
| Manual test registration | Auto-discovery (naming convention) |

---

## Q&A / Key Insights

### Q: What's the difference between Unit Test and Integration Test?
**A:** Unit tests test a single function/class in isolation — fast, many, precise. Integration tests test multiple modules together — slower, few, for overall system confidence. Both use pytest.

### Q: How does pytest pass fixtures to tests?
**A:** pytest looks at the **parameter name** of the test function, finds a fixture with the same name, calls the fixture function, takes the return value, and passes it as an argument. This is called Dependency Injection.

### Q: What does `yield` mean in a fixture?
**A:** `yield` lets a fixture do work **before** the test (setup — code before yield) and **after** the test (cleanup — code after yield). `yield` passes a value to the test and suspends the fixture function. After the test finishes, the fixture resumes. Full coverage of `yield` and Generators is in Chapter 13 (Advanced Topics).

### Q: What is fixture scope?
**A:** It defines how often a fixture is created. `function` (default) = once per test. `module` = once per test file. `session` = once per test run. You'll see practical examples in real projects.

### Q: Why must `parametrize` come immediately before the test function?
**A:** `@pytest.mark.parametrize` is a decorator, and Python requires decorators to be placed directly before the function they decorate. This is a Python language rule.

### Q: How does `pytest.raises` work?
**A:** It checks whether the code inside the `with` block raises the expected exception. If it does → test passes. If it doesn't, or raises a different exception → test fails.

### Q: What's the difference between `skip` and `xfail`?
**A:** `skip` doesn't run the test at all. `xfail` runs the test — if it fails, shows yellow (expected). If it passes, shows green (XPASS — bug may be fixed).