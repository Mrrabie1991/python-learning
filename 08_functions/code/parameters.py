# 08_functions/code/parameters.py
# How parameters work in Python — everything is passed by reference

# ---- Immutable parameter (like const & in C++) ----
def increment(x):
    """Demonstrates that immutable parameters can't be modified."""
    x = x + 1  # Rebinds x to a new object — original is untouched
    return x

num = 5
result = increment(num)
print(f"num: {num}, result: {result}")  # num: 5, result: 6

# ---- Mutable parameter (like & in C++) ----
def append_item(lst, item):
    """Demonstrates that mutable parameters CAN be modified."""
    lst.append(item)  # Modifies the original object — NOT rebinding

numbers = [1, 2, 3]
append_item(numbers, 4)
print(numbers)  # [1, 2, 3, 4] — original changed!