# 13_advanced_topics/code/05_type_hints/type_hints_callable.py

from typing import Callable


# A function that takes a function
def apply_twice(func: Callable[[int], int], value: int) -> int:
    """Apply func to value, then apply func again to the result."""
    return func(func(value))


# A function that returns a function
def make_multiplier(factor: int) -> Callable[[int], int]:
    """Return a function that multiplies by factor."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier


# Usage
def double(x: int) -> int:
    return x * 2

print(apply_twice(double, 5))  # 20 — double(double(5)) = double(10)

times_three = make_multiplier(3)
print(times_three(10))  # 30