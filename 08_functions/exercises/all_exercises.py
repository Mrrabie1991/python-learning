# 08_functions/exercises/all_exercises.py
# Chapter 08 Exercises — Functions

# ============================================================
# Exercise 8.1: Simple Functions
# ============================================================

def add(a, b):
    """Return sum of two numbers."""
    return a + b


def greet(name, greeting="Hello"):
    """Print a greeting."""
    print(f"{greeting}, {name}!")


print(add(3, 5))
greet("Ali")
greet("Sara", greeting="Hi")

print("\n","="*40,"\n")


# ============================================================
# Exercise 8.2: Parameters and Return Values
# ============================================================

def calculate_area(length, width):
    """Return area of a rectangle."""
    return length * width


def is_even(num):
    """Return True if num is even."""
    return num % 2 == 0


print(f"Area: {calculate_area(5, 4)}")
print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")

print("\n","="*40,"\n")


# ============================================================
# Exercise 8.3: *args and **kwargs
# ============================================================

def sum_all(*args):
    """Return sum of any number of arguments."""
    return sum(args)


def print_info(**kwargs):
    """Print all key-value pairs."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

print("Info:")
print_info(name="Ali", age=25, city="Tehran")

print("\n","="*40,"\n")


# ============================================================
# Exercise 8.4: Lambda
# ============================================================

# Lambda for square
square = lambda x: x * x

# Lambda for even check
is_even_lambda = lambda x: x % 2 == 0

print(f"Square of 6: {square(6)}")
print(f"Is 8 even? {is_even_lambda(8)}")

# Sort list of tuples by second element
points = [(3, 5), (1, 9), (4, 2), (7, 6)]
sorted_points = sorted(points, key=lambda p: p[1])
print(f"Sorted by second element: {sorted_points}")

print("\n","="*40,"\n")


# ============================================================
# Exercise 8.5: Calculator
# ============================================================

def calculator(a, b, operation):
    """Perform basic arithmetic based on operation string."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Unknown operation"


print(f"add(10, 5): {calculator(10, 5, 'add')}")
print(f"subtract(10, 5): {calculator(10, 5, 'subtract')}")
print(f"multiply(10, 5): {calculator(10, 5, 'multiply')}")
print(f"divide(10, 5): {calculator(10, 5, 'divide')}")
print(f"divide(10, 0): {calculator(10, 0, 'divide')}")
print(f"unknown: {calculator(10, 5, 'power')}")