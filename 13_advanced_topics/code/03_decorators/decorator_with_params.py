# 13_advanced_topics/code/03_decorators/decorator_with_params.py

def repeat(n):
    """Decorator factory — a function that returns a decorator."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)  # Run the function 3 times
def say_hello():
    print("Hello!")


say_hello()
# Hello!
# Hello!
# Hello!