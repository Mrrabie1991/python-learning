# 06_dictionaries/code/sets.py
# set — unordered collection of unique elements

# Creating sets
fruits = {"apple", "banana", "cherry"}
empty = set()  # NOT {} — that creates an empty dict
print(f"Fruits: {fruits}")

# Adding and removing
fruits.add("orange")
fruits.remove("banana")  # KeyError if not found
fruits.discard("mango")  # No error if not found
print(f"Updated: {fruits}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Union: {a | b}")            # {1, 2, 3, 4, 5, 6}
print(f"Intersection: {a & b}")     # {3, 4}
print(f"Difference: {a - b}")       # {1, 2}
print(f"Symmetric diff: {a ^ b}")   # {1, 2, 5, 6}

# Membership — O(1) average
print(f"'apple' in fruits: {'apple' in fruits}")