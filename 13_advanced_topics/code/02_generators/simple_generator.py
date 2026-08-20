# 13_advanced_topics/code/02_generators/simple_generator.py

def count_up_to(n):
    """Generate numbers from 1 to n, one at a time."""
    i = 1
    while i <= n:
        yield i    # Return i and pause
        i += 1

# Calling creates a generator object (does NOT execute the function!)
g = count_up_to(3)
print(type(g))  # <class 'generator'>

# Use next() to get values
print(next(g))  # 1 — function runs, reaches yield, returns 1, pauses
print(next(g))  # 2 — resumes after yield, increments i, yields again
print(next(g))  # 3
# print(next(g))  # StopIteration — while loop ended, function returned