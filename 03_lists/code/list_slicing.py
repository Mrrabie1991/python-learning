# 03_lists/code/list_slicing.py
# Slicing — a Python superpower with no direct C++ equivalent

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntax: list[start:stop:step]
# start: inclusive, stop: exclusive (like C++ iterators)

print(f"numbers[2:5]: {numbers[2:5]}")     # [2, 3, 4] — indices 2 to 4
print(f"numbers[:4]: {numbers[:4]}")       # [0, 1, 2, 3] — from start to 3
print(f"numbers[6:]: {numbers[6:]}")       # [6, 7, 8, 9] — from 6 to end
print(f"numbers[::2]: {numbers[::2]}")     # [0, 2, 4, 6, 8] — every 2nd
print(f"numbers[::-1]: {numbers[::-1]}")   # [9, 8, 7, ..., 0] — reverse!

# In C++, this would require a loop or std::copy