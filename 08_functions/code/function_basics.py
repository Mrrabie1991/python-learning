# 08_functions/code/function_basics.py
# Function definition in Python vs C++

# ---- Basic function ----
# C++:
# int add(int a, int b) {
#     return a + b;
# }

def add(a, b):
    """Return the sum of a and b."""  # docstring — like /** ... */ in C++
    return a + b

print(add(3, 5))  # 8

# ---- No return value (like void) ----
# C++:
# void greet(string name) {
#     cout << "Hello, " << name << endl;
# }

def greet(name):
    """Print a greeting. Returns None implicitly."""
    print(f"Hello, {name}!")

result = greet("Ali")  # "Hello, Ali!"
print(result)  # None — like returning nothing in void function