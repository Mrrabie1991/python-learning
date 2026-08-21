# Chapter 02 Exercises — Variables & Simple Data Types

## Exercise Goals

These exercises are designed to reinforce the following concepts:

- Simple data types (`int`, `float`, `str`, `bool`, `None`)
- Name Binding model (names point to objects, not memory boxes)
- Immutability
- Difference between `is` and `==`
- Integer caching in CPython

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 2.1 | Exploring Data Types | `type()` and `id()` |
| 2.2 | Type Conversion | `int()`, `float()`, `str()` |
| 2.3 | Immutability | Attempting to modify `int` and `str` |
| 2.4 | `is` vs `==` | Identity vs value comparison |
| 2.5 | Memory Analysis | Integer caching |

## Key Takeaways

- `type(x)` returns the type of the object.
- `id(x)` shows the memory address of the object.
- `int(3.99)` truncates the decimal part — it does not round.
- Integers from -5 to 256 are cached in CPython — `x = 5` and `y = 5` point to the same object.
- `==` compares values, `is` compares identity.

## Expected Output

Each file should run without errors and print `type` and `id` for various variables.