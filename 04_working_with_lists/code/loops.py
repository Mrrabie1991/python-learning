# 04_working_with_lists/code/loops.py
# Python for loops — compared to C++ range-based for

fruits = ["apple", "banana", "cherry", "orange"]

# ---- Python: for item in list ----
# C++ equivalent: for (const auto& item : fruits)
for fruit in fruits:
    print(fruit)

# ---- Python: for with index — enumerate() ----
# C++ equivalent: for (int i = 0; i < fruits.size(); i++)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# ---- Python: range() for numeric loops ----
# C++ equivalent: for (int i = 0; i < 10; i++)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop, step)
# like for (int i = 2; i < 10; i += 2)
for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8