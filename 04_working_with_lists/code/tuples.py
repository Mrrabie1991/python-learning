# 04_working_with_lists/code/tuples.py
# Tuple — an immutable list

# ---- Creating tuples ----
point = (3, 4)
coordinates = 10, 20  # parentheses are optional
single = (42,)  # comma is required for single-element tuple

print(f"point: {point}, type: {type(point)}")
print(f"coordinates: {coordinates}")

# ---- Indexing — like list ----
print(f"point[0]: {point[0]}, point[1]: {point[1]}")

# ---- Immutable — cannot modify ----
# point[0] = 5  # ERROR — tuple is immutable

# ---- Unpacking — تجزیه به متغیرها ----
x, y = point
print(f"x = {x}, y = {y}")

# ---- Swapping without temp variable ----
a, b = 1, 2
a, b = b, a
print(f"a = {a}, b = {b}")  # a=2, b=1 — swap in one line!

# ---- tuple from list, list from tuple ----
nums = [1, 2, 3]
t = tuple(nums)  # list -> tuple
lst = list(t)    # tuple -> list
print(f"tuple: {t}, list: {lst}")