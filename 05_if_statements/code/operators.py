# 05_if_statements/code/operators.py
# Comparison and logical operators

# Comparison operators (same as C++)
print(5 == 5)    # True
print(5 != 3)    # True
print(5 > 3)     # True
print(5 < 3)     # False
print(5 >= 5)    # True
print(5 <= 3)    # False

# Logical operators (keywords instead of &&, ||, !)
a, b = True, False
print(a and b)   # False — equivalent to &&
print(a or b)    # True  — equivalent to ||
print(not a)     # False — equivalent to !

# Chained comparisons — not available in C++
x = 5
print(2 < x < 10)   # True — equivalent to: 2 < x and x < 10
print(10 < x < 20)  # False