# Exercise 4.2: List Comprehension Basics

numbers = list(range(1, 11))

# Squares of all numbers
squares = [x * x for x in numbers]
print(f"squares : {squares}")

# Filter even numbers
even_numbers = [i for i in numbers if i % 2 == 0]
print(f"even numbers : {even_numbers}")
# Why can't we unpack in f-string? Because unpacking (*) only works
# in function calls, not inside f-strings.

# Labels for even/odd
labels = ["even" if i % 2 == 0 else "odd" for i in numbers]
print(labels)