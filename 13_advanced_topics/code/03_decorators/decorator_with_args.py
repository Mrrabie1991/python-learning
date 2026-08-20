# 13_advanced_topics/code/03_decorators/decorator_with_args.py

def log_arguments(func):
    """Print arguments before executing the function."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_arguments
def add(a, b):
    return a + b


@log_arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(add(3, 5))
# Calling add with args=(3, 5), kwargs={}
# add returned 8
# 8

print(greet("Ali", greeting="Hi"))
# Calling greet with args=('Ali',), kwargs={'greeting': 'Hi'}
# greet returned Hi, Ali!
# Hi, Ali!