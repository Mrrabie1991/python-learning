# 02_variables_types/exercises/exercise_04.py

# Two lists with same content
a = [1, 2]
b = [1, 2]

print(f"a == b : {a == b}")  # True — values are equal
print(f"a is b : {a is b}")  # False — different objects in memory

# Two small integers (cached by Python)
x = 5
y = 5

print(f"x == y : {x == y}")  # True — values are equal
print(f"x is y : {x is y}")  # True — same cached object!