# 03_lists/code/list_basics.py
# Python list — equivalent to std::vector but far more flexible

# ---- Part 1: Creating lists ----
# C++: std::vector<int> v = {1, 2, 3, 4, 5};
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14, True, None]  # heterogeneous — impossible in std::vector
empty = []

print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"empty: {empty}")

# ---- Part 2: Indexing (zero-based, like C++) ----
# C++: v[0], v[1], ...
print(f"\nnumbers[0]: {numbers[0]}")
print(f"numbers[4]: {numbers[4]}")
print(f"numbers[-1]: {numbers[-1]}")  # negative index: last element (no C++ equivalent)

# ---- Part 3: Mutability — THIS IS NEW ----
# Unlike int and str, list contents CAN be changed
numbers[0] = 99
print(f"\nAfter numbers[0] = 99: {numbers}")

# Compare with str (immutable):
s = "Hello"
# s[0] = "h"  # ERROR — str is immutable

# ---- Part 4: Common methods ----
fruits = ["apple", "banana", "cherry"]

# append — like push_back in C++
fruits.append("orange")
print(f"\nAfter append: {fruits}")

# insert at specific position
fruits.insert(1, "mango")
print(f"After insert at index 1: {fruits}")

# remove by value
fruits.remove("banana")
print(f"After remove 'banana': {fruits}")

# pop — remove and return last element (or by index)
last = fruits.pop()
print(f"Popped: {last}, remaining: {fruits}")

# len — number of elements (like .size() in C++)
print(f"\nLength: {len(fruits)}")

# in — check existence
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")