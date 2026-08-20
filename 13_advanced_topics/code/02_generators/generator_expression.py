# 13_advanced_topics/code/02_generators/generator_expression.py

# List comprehension — creates all values in memory at once
squares_list = [i * i for i in range(10)]
print(squares_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expression — produces values one at a time (parentheses instead of brackets)
squares_gen = (i * i for i in range(10))
print(squares_gen)   # <generator object <genexpr> at 0x...>

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(list(squares_gen))  # [4, 9, 16, 25, 36, 49, 64, 81] — the rest