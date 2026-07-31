# 05_if_statements/code/ternary.py
# Ternary operator — conditional expression

x = 10

# Python: true_val if condition else false_val
# C++:    condition ? true_val : false_val
result = 100 if x > 5 else 200
print(result)  # 100

# With different values
status = "pass" if x >= 10 else "fail"
print(status)  # pass

# Equivalent if-else (for comparison)
if x >= 10:
    status2 = "pass"
else:
    status2 = "fail"