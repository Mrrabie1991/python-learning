# 08_functions/code/default_args.py
# Default arguments — like C++ default parameters

# C++:
# void greet(string name, string greeting = "Hello") {
#     cout << greeting << ", " << name << endl;
# }

def greet(name, greeting="Hello"):
    """Print a greeting. greeting defaults to 'Hello'."""
    print(f"{greeting}, {name}!")

greet("Ali")              # Hello, Ali!
greet("Sara", "Hi")       # Hi, Sara!

# DANGER — mutable default is evaluated ONCE at function definition
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] — WTF?! Shared list!
print(add_item(3))  # [1, 2, 3]

# راه درست
def add_item_correct(item, lst=None):
    if lst is None:
        lst = []  # Create new list for each call
    lst.append(item)
    return lst

print(add_item_correct(1))  # [1]
print(add_item_correct(2))  # [2]