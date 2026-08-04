# 08_functions/code/lambda_demo.py
# Lambda functions — anonymous, one-expression functions

# C++ lambda:
# auto add = [](int a, int b) { return a + b; };

# Python lambda — only one expression, no statements
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Common use case — key function for sorting
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Reza", "score": 78},
]

# Sort by score — lambda as key
sorted_by_score = sorted(students, key=lambda s: s["score"])
print(sorted_by_score)
# [{'name': 'Reza', 'score': 78}, {'name': 'Ali', 'score': 85}, {'name': 'Sara', 'score': 92}]

# Lambda in map/filter — functional style
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10]
print(f"Evens: {evens}")      # [2, 4]