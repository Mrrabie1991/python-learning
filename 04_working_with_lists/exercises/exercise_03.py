# Exercise 4.3: Working with Tuple


point = (3, 4)

x, y = point
print(f"x = {x} --- y = {y}")

a, b = 10, 20
print(f"a = {a} --- b = {b}")

# Swap without temp variable
b, a = a, b
print(f"a = {a} --- b = {b}")

list_number = [1, 2, 3]
tuple_number = (4, 5, 6)

print(tuple(list_number))
print(list(tuple_number))