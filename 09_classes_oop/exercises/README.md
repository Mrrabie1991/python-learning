# Chapter 09 Exercises — Classes & OOP (Pythonic)

## Exercise Goals

These exercises reinforce the following concepts:

- Defining classes and methods with `self`
- Constructor (`__init__`) and instance attributes
- Property for controlled access
- Magic Methods for operator overloading
- Composition over Inheritance

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 9.1 | Simple Class | `class`, methods with `self` |
| 9.2 | Constructor and self | `__init__`, instance attributes |
| 9.3 | Property | `@property`, computed property |
| 9.4 | Magic Methods | `__str__`, `__add__`, `__eq__` |
| 9.5 | Composition | has-a relationship |

## Key Takeaways

- Every class method must take `self` as the first parameter.
- `self` means "this specific instance" — without it, Python cannot tell which instance an attribute belongs to.
- `@property` turns a function into a read-only attribute.
- Magic Methods are the Python equivalent of C++ operator overloading.
- Composition means "an object contains another object" — more flexibility than Inheritance.

## Expected Output

Each file should run without errors and print method results, property values, operator behavior, and Composition results.