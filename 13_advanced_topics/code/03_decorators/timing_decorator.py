# 13_advanced_topics/code/03_decorators/timing_decorator.py

import time


def measure_time(func):
    """Measure and print execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@measure_time
def slow_function():
    """A slow function for testing."""
    time.sleep(1.5)
    return "Done"


print(slow_function())
# slow_function took 1.5001 seconds
# Done