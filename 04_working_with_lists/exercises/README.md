# Chapter 04 Exercises — Working with Lists

## Exercise Goals

These exercises reinforce the following concepts:

- `for` loops and `enumerate` for list iteration
- List Comprehension for building and filtering lists
- Working with `tuple` and unpacking
- Data combination tools (`zip`)
- Simple data analysis with loops and comprehension

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 4.1 | Iterating and Transforming Lists | `for`, `enumerate`, `lower()` |
| 4.2 | List Comprehension Basics | `[expr for x in list if cond]` |
| 4.3 | Working with Tuple | unpacking, swap without temp variable |
| 4.4 | zip and enumerate | Pairing data |
| 4.5 | Simple Data Analysis | Filtering, average, finding max/min with loop |

## Key Takeaways

- Unpacking with `*` is only allowed in function arguments, not inside f-strings.
- `sorted(list)` does not modify the original list; `list.sort()` does.
- `zip` works until the shortest list when lengths differ.
- Swapping two variables in Python: `a, b = b, a`.
- To find max/min with a loop, initialize from the first element.

## Expected Output

Each file should run without errors and print transformed lists, paired data, and analysis results.