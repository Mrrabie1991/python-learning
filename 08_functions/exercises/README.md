# Chapter 08 Exercises — Functions

## Exercise Goals

These exercises reinforce the following concepts:

- Defining functions with `def` and default parameters
- Returning values with `return`
- Variable arguments with `*args` and `**kwargs`
- Anonymous functions with `lambda`
- Error handling in functions

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 8.1 | Simple Functions | `def`, default parameter |
| 8.2 | Parameters and Return | `return`, simple condition |
| 8.3 | `*args` and `**kwargs` | Variable arguments |
| 8.4 | Lambda | Anonymous functions, `sorted` with `key` |
| 8.5 | Calculator | Operation selection, division by zero handling |

## Key Takeaways

- Default parameter: `def greet(name, greeting="Hello")`.
- `*args` creates a tuple of positional arguments.
- `**kwargs` creates a dict of keyword arguments.
- `sorted(points, key=lambda p: p[1])` sorts by the second tuple element.
- Handle division by zero: check `if b == 0` before dividing.

## Expected Output

The program runs all sections and prints function results, lambda sorting, and calculator behavior.