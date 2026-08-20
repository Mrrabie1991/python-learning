# 13_advanced_topics/code/03_decorators/simple_decorator.py

# Step 1: A function that takes a function and returns a new function
def my_decorator(func):
    """Create a wrapper around func."""
    def wrapper():
        print("Something BEFORE the function")
        func()
        print("Something AFTER the function")
    return wrapper  # Return the new function


# Step 2: A normal function
def say_hello():
    print("Hello!")


# Step 3: Wrap the function with decorator
say_hello = my_decorator(say_hello)  # say_hello is now wrapper

# Step 4: Call it
say_hello()


@my_decorator
def say_hi():
    print("Hi!")

say_hi()