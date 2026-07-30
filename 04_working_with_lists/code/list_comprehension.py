# 04_working_with_lists/code/list_comprehension.py
# List Comprehension — one-liners that replace multi-line loops

nums = [1, 2, 3, 4, 5]

# ---- Basic: [expression for item in list] ----
squares = [n * n for n in nums]
print(f"Squares: {squares}")  # [1, 4, 9, 16, 25]

# ---- With condition: [expression for item in list if condition] ----
evens = [n for n in nums if n % 2 == 0]
print(f"Evens: {evens}")  # [2, 4]

# ---- With if-else: [expr_if if condition else expr_else for item in list] ----
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
print(f"Labels: {labels}")  # ['odd', 'even', 'odd', 'even', 'odd']

# ---- Nested loops — ترکیب دو لیست ----
colors = ["red", "blue"]
objects = ["car", "bike"]
combinations = [f"{c} {o}" for c in colors for o in objects]
print(f"Combinations: {combinations}")
# ['red car', 'red bike', 'blue car', 'blue bike']

# ---- Calling functions ----
names = ["ALICE", "BOB", "CHARLIE"]
lower = [name.lower() for name in names]
print(f"Lower: {lower}")  # ['alice', 'bob', 'charlie']