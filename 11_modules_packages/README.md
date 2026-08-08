# 11 - Modules, Packages & Project Structure

This chapter answers the question: **"Where should I put the code of a real project so that I, others, and tools all understand it?"**

There are seven core concepts: Module, Import, `if __name__ == "__main__"`, Package, Relative Import, Virtual Environment & pip, Project Structure & pyproject.toml.

---

## 1. Module

### Why Modules?

You have a 1000-line file. Finding a function takes 5 minutes. Changing one section might break another.

**Solution:** Split code into small, related files.

### What is a Module?

**A `.py` file.** Nothing more. Every Python file is a module.

**Comparison with C++:**
- C++: one `.cpp` + one `.h` = one code unit (interface separate from implementation).
- Python: one `.py` = one module (both interface and implementation).

### Creating a Module

```python
# calculator.py
# This file IS a module. Its name is 'calculator'.

PI = 3.14159  # Module-level variable

def add(a, b):
    """Return sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return product of two numbers."""
    return a * b
```

---

## 2. Import

### Why Import?

You've created `calculator.py`. How do you use it in another file?

### What is Import?

A statement that **executes** a module and creates a **module object** from it.

**Difference from C++:**
- `#include "file.h"` — copies the file's content. Everything in `file.h` lands directly in the current scope.
- `import module` — executes the `.py` file, creates a module object, and functions/variables are accessed through that object. A namespace is automatically created.

### Three Import Styles

```python
# Style 1: import the entire module (most Pythonic — clear where everything comes from)
import calculator
calculator.add(3, 5)

# Style 2: import with alias (for long names)
import calculator as calc
calc.add(3, 5)

# Style 3: import specific things (when you only need a few)
from calculator import add, subtract
add(3, 5)  # No calculator. prefix — directly in scope

# Style 4: import everything (not Pythonic — pollutes namespace, avoid!)
from calculator import *
```

**Pythonic Principle:** Prefer `import module`. Forget `from module import *`.

---

## 3. `if __name__ == "__main__"`

### Why?

You want `calculator.py` to be **both runnable directly** (for testing) **and importable** (for use in other files). How do you activate test code only in direct execution mode?

### What is `__name__`?

Python defines an automatic variable called `__name__` for every file:

- If the file is executed **directly** (`python calculator.py`) → `__name__` equals `"__main__"`.
- If the file is **imported** (`import calculator`) → `__name__` equals `"calculator"` (the module name).

### Creating

```python
# calculator_with_test.py
# This file can be BOTH imported AND run directly

PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test code — only runs when file is executed directly
if __name__ == "__main__":
    print("Testing calculator module:")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"PI = {PI}")
```

```bash
# Direct execution — test code runs
python calculator_with_test.py

# Import — test code does NOT run
python -c "import calculator_with_test; print(calculator_with_test.add(2, 3))"
```

---

## 4. Package

### Why Packages?

Your project has 20 modules. All dumped in one folder. It's a mess. You don't know which module belongs to which part of the project.

**Solution:** Put related modules in **separate folders**. These folders are called Packages.

### What is a Package?

A **folder** containing an `__init__.py` file. That's it.

**Comparison with C++:**
- C++: `namespace sensors { class Camera { }; }`
- Python: folder `sensors/` (package) with file `camera.py` (module) inside.

### What is `__init__.py`?

A file that tells Python "this folder is a package, you can import it."

- Can be **completely empty**.
- Can contain **initialization code** (e.g., importing submodules for easier access).

### Package Structure

```
robot/                  # Package (folder)
├── __init__.py         # This file makes the folder a package
├── sensors.py          # Module (.py file)
└── navigation.py       # Module (.py file)
```

### Creating

```python
# robot/__init__.py
from .sensors import Camera, Motor

__version__ = "0.1.0"
```

```python
# robot/sensors.py

class Camera:
    def __init__(self, resolution=(1920, 1080)):
        self.resolution = resolution

    def read(self):
        return f"Camera: image at {self.resolution}"

class Motor:
    def __init__(self, max_speed=100):
        self.max_speed = max_speed

    def set_speed(self, speed):
        return f"Motor: speed set to {min(speed, self.max_speed)}"
```

```python
# robot/navigation.py

class PathPlanner:
    def plan(self, start, goal):
        return f"Path planned from {start} to {goal}"

class Localizer:
    def get_position(self):
        return (0, 0)
```

```python
# Using the package

from robot.sensors import Camera
cam = Camera()
print(cam.read())

from robot import Motor  # re-exported in __init__.py
motor = Motor()
print(motor.set_speed(50))
```

### What is `__all__`?

A list of names that defines exactly what gets imported when someone writes `from package import *`. Like `public:` in C++.

```python
# robot/__init__.py
__all__ = ["Camera", "Motor", "PathPlanner"]

# Now:
# from robot import * → only Camera, Motor, PathPlanner
```

---

## 5. Relative Import

### Why?

In `robot/navigation.py`, you want to use `robot/sensors.py`. If you rename the package (`robot` → `my_robot`), absolute imports break.

**Solution:** Relative import — address relative to the current file's location.

```python
# robot/navigation.py — with relative import

from .sensors import Camera  # . means this folder (robot/)

class PathPlanner:
    def __init__(self):
        self.camera = Camera()

    def plan(self, start, goal):
        image = self.camera.read()
        return f"Using {image} | Path from {start} to {goal}"
```

### Notation

| Symbol | Meaning | Example |
|---|---|---|
| `.` | Current package | `from .sensors import Camera` |
| `..` | Parent package | `from ..utils import helper` |
| `...` | Grandparent package | `from ...common import config` |

---

## 6. Virtual Environment & pip

### Why?

Project A needs `numpy==1.21`. Project B needs `numpy==1.26`. Installing both system-wide creates version conflicts.

**Solution:** Create an **isolated environment** (Virtual Environment) for each project.

**Comparison with C++:**
- C++: each project manages libraries in a `Dependencies/` folder or via Conan/vcpkg.
- Python: each project has a `venv/` — an isolated copy of Python and its libraries.

### Step by Step

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate (Linux / Git Bash)
source venv/bin/activate
# Windows PowerShell:
# .\venv\Scripts\Activate.ps1

# 3. Install a library
pip install requests

# 4. List installed packages
pip list

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Deactivate
deactivate

# 7. Rebuild environment on another system
# source venv/bin/activate
# pip install -r requirements.txt
```

### Philosophy

- The `venv/` folder should **never** be committed to git (it's in `.gitignore`).
- Only commit `requirements.txt` (or `pyproject.toml`).
- Anyone cloning the project rebuilds the identical environment with `pip install -r requirements.txt`.

---

## 7. Standard Project Structure & pyproject.toml

### Why?

A real project is more than just code. It has tests, data, documentation, dependencies. All must have a clear place. You also want to install the project like a library so it can be imported from anywhere.

### Standard Structure

```
my_robot/                    # Repository root
├── src/                     # Main source code
│   └── my_robot/            # Python package
│       ├── __init__.py      # __version__ lives here
│       ├── main.py          # Entry point
│       ├── core.py          # Core logic
│       ├── sensors/         # Sensors package
│       │   ├── __init__.py
│       │   ├── camera.py
│       │   └── lidar.py
│       ├── navigation/      # Navigation package
│       │   ├── __init__.py
│       │   ├── planner.py
│       │   └── controller.py
│       └── utils.py         # Shared helper functions
├── tests/                   # Tests (separate from source)
│   ├── __init__.py
│   ├── test_camera.py
│   └── test_planner.py
├── data/                    # Data files (not code)
├── venv/                    # Virtual environment (gitignored)
├── .gitignore
├── README.md
├── requirements.txt         # Dependencies (simple)
└── pyproject.toml           # Project configuration (modern)
```

### What is `pyproject.toml`?

The **project identity card** — a modern replacement for several old files. A text file in TOML format.

**Before:** Python projects had multiple config files (`setup.py`, `setup.cfg`, `requirements.txt`).
**Now:** `pyproject.toml` consolidates them all.

### Main Sections

```toml
# Section 1: build system — always the same, copy as-is
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

# Section 2: project metadata
[project]
name = "my_robot"
version = "0.1.0"
description = "A demo robot package"
requires-python = ">=3.9"
dependencies = [
    "numpy>=1.24",
    "requests>=2.28",
]             # Required libraries

# Section 3: optional dependencies — dev tools
[project.optional-dependencies]
dev = ["pytest>=7.0"]

# Section 4: if your package is in src/
[tool.setuptools.packages.find]
where = ["src"]

# Section 5: tool settings
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
```

### Writing `pyproject.toml` — A Quick Guide

`pyproject.toml` is like `CMakeLists.txt` in C++ — learn the template once, then only change `name` and `dependencies` for each new project.

- **`[build-system]` section:** Always the same. Every project uses this.
- **`[project]` section:** Only change `name` and `dependencies`.
- **`[tool.setuptools.packages.find]` section:** Include this if your package is inside `src/`. Otherwise, remove it.
- **`[tool.*]` sections:** Only include if you use those tools.

### `pip install` Variants

| Command | Purpose | Behavior |
|---|---|---|
| `pip install numpy` | Install public library | Copies to site-packages |
| `pip install .` | Install project for **usage** | Copies to site-packages |
| `pip install -e .` | Install project for **development** | Links to source folder — live changes |
| `pip install -e .[dev]` | Install dev + dev tools | As above + pytest, black |

### What Does `-e` (editable) Mean?

**Without `-e`:** Python **copies** project code to `site-packages/`. If you change your code, changes are not reflected — you must `pip install` again.

**With `-e`:** Python **does not copy**. It creates a link to the project folder. Any code change is **immediately** reflected everywhere. Meant for development time.

### What Does `.` Mean?

`.` = the current folder (the one containing `pyproject.toml`).

### `pip install` and Dependencies

- `pip install .` ← reads `pyproject.toml`, installs `dependencies` **automatically**.
- `pip install -r requirements.txt` ← only reads `requirements.txt`. Must be run **manually**.
- If a project has `pyproject.toml`, `pip install .` is sufficient.

### What Does `[dev]` Mean?

Optional dependencies. End users don't need pytest. Only developers install `[dev]`.

```bash
pip install -e .            # Only numpy, requests
pip install -e .[dev]       # numpy, requests + pytest, black
```

### What Does `python -m my_robot.main` Mean?

Runs a **module** (not a file). `-m` stands for module. Python searches for `my_robot.main` in `sys.path` and runs it.

```bash
# Run a file by path
python src/my_robot/main.py

# Run a module (after pip install -e .)
python -m my_robot.main      # Works from anywhere in the system
```

---

## Summary

| # | Concept | In One Line | C++ Equivalent |
|---|---|---|---|
| 1 | **Module** | A `.py` file | `.cpp` + `.h` file |
| 2 | **Import** | Executes module, creates module object | `#include` (fundamentally different) |
| 3 | **`if __name__ == "__main__"`** | Code that only runs on direct execution | Separate file with `main()` |
| 4 | **Package** | Folder with `__init__.py` | `namespace` |
| 5 | **Relative Import** | Import relative to current file | `#include "../"` |
| 6 | **venv + pip** | Isolated environment + package manager | Conan / vcpkg / Docker |
| 7 | **pyproject.toml** | Project identity card | `CMakeLists.txt` |

---

## Q&A / Key Insights

### Q: What is `__all__` and what does it do?
**A:** A list of names defining exactly what `from package import *` imports. Like `public:` in C++. It only affects `import *` — direct imports (like `from package import _internal`) still work.

### Q: What does `pip install -e .` mean?
**A:** Installs the project in editable (development) mode. `-e` means Python does not copy the code — it creates a link to the source folder. Any code change is immediately reflected everywhere. `.` means the current folder (where `pyproject.toml` is).

### Q: What is `[build-system]` in `pyproject.toml`?
**A:** Tells pip which tool to use to build the project. "Build" means reading metadata and copying (or linking) files to `site-packages/`. This is not compilation — Python is not compiled.

### Q: Does `pip install .` also install dependencies?
**A:** If the project has `pyproject.toml`, yes — it reads the `dependencies` section and installs them automatically. If it only has `requirements.txt`, no — you must run `pip install -r requirements.txt` separately.

### Q: What is `[dev]` in `pip install -e .[dev]`?
**A:** Optional dependencies defined in `pyproject.toml` under `[project.optional-dependencies]`. `dev` typically includes development tools (pytest, black, mypy). Regular users don't need them.

### Q: What does `python -m my_robot.main` mean?
**A:** Runs a module (not a file). `-m` stands for module. Python searches `sys.path` for `my_robot.main`. `.main` means `main.py` inside the `my_robot/` package. After `pip install -e .`, this command works from anywhere.

### Q: How do I write a `pyproject.toml`?
**A:** It has a fixed template. The `[build-system]` section is always the same. Fill in `[project]` with your `name` and `dependencies`. If your package is in `src/`, add `[tool.setuptools.packages.find]`. Like `CMakeLists.txt` — learn once, copy for new projects.

### Q: Does Python produce executable files (exe) like C++?
**A:** No. Python runs `.py` files (text) directly. For distribution, you can use PyInstaller to create an executable, or distribute the source code as-is. Python's philosophy embraces open-source code.

### Q: Why write `__version__ = "0.1.0"` in `__init__.py`?
**A:** It's a convention for storing the project version. `__init__.py` is the first thing executed when a package is imported, so `__version__` is always available: `import my_robot; print(my_robot.__version__)`. Automated tools (like pip) sometimes read the version from here.