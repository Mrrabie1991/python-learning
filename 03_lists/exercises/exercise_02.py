# Exercise 3.2: Removing from List
# Requirements:
# - Create a list of numbers 1 to 10
# - Remove number 5 with remove()
# - Pop the last element and print it
# - Delete element at index 2 with del
# - Print the final list

numbers = list(range(1, 11))

print(numbers)

numbers.remove(5)
print(numbers)

last_number = numbers.pop()
print(f"last number popped : {last_number} and updated list : {numbers}")

del numbers[2]
print(numbers)