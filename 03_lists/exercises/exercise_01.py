# Exercise 3.1: Basic List Operations
# Requirements:
# - Create a list of 5 fruits
# - Print first and last element (use negative index for last)
# - Append a fruit to the end
# - Insert a fruit at position 2
# - Print list length

fruits = ["orange", "watermelon", "blueberry", "strawberry", "sour cherry"]

print(f"fruits[0] : {fruits[0]} and fruits[-1] : {fruits[-1]}")

fruits.append("banana")
print(f"fruits after append : {fruits}")

fruits.insert(1, "apple")
print(f"fruits after insert at position 2 : {fruits}")

print(f"length of fruits : {len(fruits)}")