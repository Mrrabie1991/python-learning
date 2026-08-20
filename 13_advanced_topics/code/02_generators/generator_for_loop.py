# 13_advanced_topics/code/02_generators/generator_for_loop.py

def fibonacci(limit):
    """Generate Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Usage in a for loop — Python calls next() automatically
for num in fibonacci(100):
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34 55 89