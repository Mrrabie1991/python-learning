# 01 - Getting Started & Python Philosophy

## What is Python?

Python is a high-level, interpreted, general-purpose programming language created by Guido van Rossum in 1991. Its core design philosophy emphasizes code readability and developer productivity.

### Design Philosophy: Python vs C++

| Aspect        | C++                                    | Python                                |
|---------------|----------------------------------------|---------------------------------------|
| Primary Goal  | Power, speed, hardware control         | Simplicity, readability, dev speed    |
| Creator       | Bjarne Stroustrup                      | Guido van Rossum                      |
| Motto         | "You only pay for what you use"        | "Readability counts"                  |

## Interpreter vs Compiler

### C++ Model (Compiled)

Source (.cpp) -> Compiler -> Machine Code -> Execution

- Entire code translated to machine code at once.
- Errors caught at compile-time.
- Requires a build system (CMake, Make).
- Very high execution speed.

### Python Model (Interpreted)

Source (.py) -> Python Interpreter -> Line-by-line execution

- Code read and executed line by line.
- Errors caught at runtime.
- No build step — change it, run it.
- Very high development speed.

**Analogy:** The interpreter is like a simultaneous translator — it reads and executes sentence by sentence. The compiler translates the entire book at once and delivers a new book.

## The Zen of Python

Run the following command:

```bash
python -c "import this"
```

Key principles:

- **Beautiful is better than ugly.**
- **Explicit is better than implicit.**
- **Simple is better than complex.**
- **Readability counts.**
- **There should be one-- and preferably only one --obvious way to do it.**

### What Does "Pythonic" Mean?

Writing code that aligns with these principles. Code that looks like it was "born in Python," not translated from another language.

## First Program — hello_world.py

### Code

```python
import sys
import platform

def main():
    print("Hello, Intelligent Systems!")
    print(f"Python version: {sys.version}")
    print(f"Running on: {platform.system()} {platform.release()}")

if __name__ == "__main__":
    main()
```

### Run Command

```bash
python hello_world.py
```

### Sample Output

```bash
Hello, Intelligent Systems!
Python version: 3.14.6 (main, ...)
Running on: Windows 11
```

### Engineering Note:
```bash
    if __name__ == "__main__"
```
This ensures main() runs only when the script is executed directly, not when imported as a module. (Analogous to int main() in C++.)

---

## Q&A / Key Insights

### Q: What's the real difference between an interpreter and a compiler? Is an interpreter like a translator?

**A:** Exactly. An interpreter is like a simultaneous translator — it reads and executes line by line. A compiler translates the whole program into machine code upfront. In Python, there's no build step, no .obj files, no linking. Change it, run it.

### Q: What does "Pythonic" mean?

**A:** It means writing code aligned with Python's philosophy (The Zen of Python): readable, simple, explicit. Code that looks like a native Python speaker wrote it, not a C++ programmer translating their habits into Python.