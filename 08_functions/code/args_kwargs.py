# 08_functions/code/args_kwargs.py
# *args and **kwargs — variable number of arguments

# ---- *args — variable positional arguments (like ... in C) ----
def sum_all(*args):
    """Return the sum of all arguments."""
    print(f"args type: {type(args)}")  # <class 'tuple'>
    return sum(args)

print(sum_all(1, 2, 3))       # 6
print(sum_all(1, 2, 3, 4, 5)) # 15

# ---- **kwargs — variable keyword arguments ----
def print_info(**kwargs):
    """Print all key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ali", age=25, city="Tehran")

# ---- Combining *args and **kwargs ----
def full_signature(required, *args, default="x", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"default: {default}")
    print(f"kwargs: {kwargs}")

full_signature("req", "a", "b", "c", default="y", name="Ali", age=25)