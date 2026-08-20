# 13_advanced_topics/code/01_iterators/iterator_manual.py

numbers = [1, 2, 3]

# iter() calls __iter__() internally
it = iter(numbers)

# next() calls __next__() internally
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration — no more elements