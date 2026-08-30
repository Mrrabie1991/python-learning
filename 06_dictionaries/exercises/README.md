# Chapter 06 Exercises — Dictionaries

## Exercise Goals

These exercises reinforce the following concepts:

- Creating and accessing `dict`
- Adding, modifying, and removing key-value pairs
- Iterating with `keys()`, `values()`, `items()`
- `dict comprehension`
- Counting elements with `dict`

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 6.1 | Creating and Accessing | `[]`, `get()`, default value |
| 6.2 | Adding and Removing | `del`, `pop()` |
| 6.3 | Iterating | `keys()`, `values()`, `items()`, average |
| 6.4 | Dict Comprehension | Building and filtering dicts |
| 6.5 | Word Counter | Counting pattern with `get(word, 0) + 1` |

## Key Takeaways

- `d.get(key, default)` is safer than `d[key]` — returns `default` instead of raising when key is missing.
- `del d[key]` only removes; `d.pop(key)` removes and returns the value.
- For counting elements: `d[word] = d.get(word, 0) + 1`.
- `dict comprehension`: `{k: v for k, v in items if condition}`.
- Swapping keys and values: `{v: k for k, v in d.items()}`.

## Expected Output

The program runs all sections and prints constructed dicts, iterated values, and counting results.