# Chapter 03 Exercises — Introducing Lists

## Exercise Goals

These exercises reinforce the following concepts:

- List creation and manipulation (`append`, `insert`, `remove`, `pop`, `del`)
- Positive and negative indexing
- Slicing with `[start:stop:step]`
- Difference between Shallow Copy and Deep Copy
- List Comprehension and matrix operations
- Iteration tools (`zip`, unpacking with `*`)

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 3.1 | Basic List Operations | `append`, `insert`, `len`, negative index |
| 3.2 | Removing from List | `remove`, `pop`, `del` |
| 3.3 | Slicing | List slicing with various steps |
| 3.4 | Shallow and Deep Copy | Difference between `copy()` and `deepcopy()` |
| 3.5 | Matrix with List Comprehension | Matrix creation, main diagonal, transpose |

## Key Takeaways

- `list(range(10))` creates numbers 0 to 9, not 1 to 10.
- `*row` in `print` prints a list without brackets and commas.
- `zip(*matrix)` creates the transpose — output is tuples, converted with `list()`.
- Shallow Copy only copies the first layer — inner layers remain shared.
- Deep Copy rebuilds all layers from scratch.

## Expected Output

Each file should run without errors and print modified lists, sliced elements, and copy comparisons.