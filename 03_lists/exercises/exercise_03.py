# Exercise 3.3: Slicing
# Requirements:
# - Create a list of numbers 0 to 9
# - Show: first three elements, last three elements,
#   elements from index 2 to 6, elements with step 2, reversed list

numbers = list(range(10))  # 0 to 9 

print(numbers[:3])    # [0, 1, 2]
print(numbers[-3:])   # [7, 8, 9]
print(numbers[2:7])   # [2, 3, 4, 5, 6]
print(numbers[::2])   # [0, 2, 4, 6, 8]
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]