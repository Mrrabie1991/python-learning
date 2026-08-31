# Chapter 10 Exercises — Files & Exceptions

## Exercise Goals

These exercises reinforce the following concepts:

- Writing and reading files with `with open()`
- Reading files line by line
- Error handling with `try-except`
- Data conversion and ignoring invalid input
- Working with CSV files

## Exercises

| Number | Title | Main Concept |
|---|---|---|
| 10.1 | Write and Read a File | `with open()`, `write()`, `read()` |
| 10.2 | Read Line by Line | `for line in file`, `enumerate` |
| 10.3 | Error Handling | `try-except FileNotFoundError` |
| 10.4 | Read Numbers | `int()` in `try-except`, ignoring errors |
| 10.5 | Simple CSV | `csv.writer`, `csv.DictReader` |

## Key Takeaways

- `with open("file.txt", "w")` creates or overwrites a file.
- `"r"` for reading, `"w"` for writing, `"a"` for appending.
- `file.read()` reads the whole file; `for line in file` reads line by line.
- `try-except` handles missing file errors.
- `csv.DictReader` converts each row to a dict — access by column name.

## Expected Output

The program creates `test.txt`, `numbers.txt`, and `people.csv`. Output includes file contents, sum of valid numbers, and CSV rows.