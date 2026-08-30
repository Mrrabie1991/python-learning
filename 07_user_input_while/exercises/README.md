# Chapter 07 Exercises — User Input & while Loops

## Exercise Goals

These exercises reinforce the following concepts:

- Getting user input with `input()`
- `while True` loop with `break`
- Input validation with `try-except`
- Collecting items until a sentinel value
- Building an interactive menu with separate functions

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 7.1 | Sum of Numbers | `while True` + `break` |
| 7.2 | Guess the Number | Hint conditions in a loop |
| 7.3 | Input Validation | `try-except ValueError` |
| 7.4 | Collecting Items | Sentinel pattern with `enumerate` |
| 7.5 | Interactive Menu | Separate functions + menu loop |

## Key Takeaways

- Standard validation pattern: `while True` + `break` after valid input.
- `input()` always returns a string — convert with `int()` or `float()` for numbers.
- `try-except` handles non-numeric input.
- Sentinel pattern: a special value (like `"done"` or `"back"`) to exit a loop.
- Separating each option's logic into its own function improves readability.

## Expected Output

The program runs all sections and prints sums, guess results, validated input, item lists, and menu behavior.