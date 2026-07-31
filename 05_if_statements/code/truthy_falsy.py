# 05_if_statements/code/truthy_falsy.py
# Truthy and falsy values in Python

# Falsy values (evaluate to False in boolean context)
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(""))       # False — empty string
print(bool([]))       # False — empty list
print(bool({}))       # False — empty dict
print(bool(set()))    # False — empty set
print(bool(()))       # False — empty tuple
print(bool(None))     # False

# Truthy values (everything else)
print(bool(1))        # True
print(bool(-1))       # True
print(bool("Hello"))  # True
print(bool([1, 2]))   # True
print(bool({"a": 1})) # True

# Practical usage — checking if a collection is empty
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")

items = []
if not items:
    print("List is empty")