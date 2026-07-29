# 03_lists/code/list_memory.py
# Demonstrating that list stores references, not objects

a = [1, 2, 3]
b = a  # b points to the SAME list object (not a copy!)

a.append(4)
print(f"a: {a}")  # [1, 2, 3, 4]
print(f"b: {b}")  # [1, 2, 3, 4] — b also changed!

print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")  # Same id — they ARE the same object
print(f"a is b: {a is b}")  # True

# To copy, use .copy() or list()
c = a.copy()  # shallow copy
a.append(5)
print(f"a: {a}")  # [1, 2, 3, 4, 5]
print(f"c: {c}")  # [1, 2, 3, 4] — unaffected

print(f"id(a): {id(a)}")
print(f"id(c): {id(c)}")  # Same id — they ARE the same object
print(f"a is c: {a is c}")  # False