# Chapter 05 Exercises — if Statements

## Exercise Goals

These exercises reinforce the following concepts:

- `if` / `elif` / `else` structure
- `match-case` with guard patterns
- Truthy and falsy values
- Ternary operator
- Logical problem solving (leap year)

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 5.1 | Simple Condition | `if` / `elif` / `else` |
| 5.2 | Grading | `if-elif-else` and `match-case` with guards |
| 5.3 | Truthy/Falsy Check | `if not input` |
| 5.4 | Ternary Operator | `value_if_true if condition else value_if_false` |
| 5.5 | Leap Year | Combined logic with `and` / `or` |

## Key Takeaways

- `match-case` with `case s if s >= 90:` creates a new variable `s` holding the match value.
- For simple comparison conditions, `if-elif-else` is more readable than `match-case`.
- Empty string (`""`), empty list (`[]`), and `None` are falsy values.
- Ternary operator: `result = "Yes" if condition else "No"`.
- Leap year: `(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)`.

## Expected Output

The program takes user input and prints condition results. Test various inputs for each section.