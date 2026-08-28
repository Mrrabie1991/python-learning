# Exercise 4.1: Iterating and Transforming Lists

names = ["ALI", "SARA", "REZA", "MARYAM", "HOSSEIN"]

# Print each name in lowercase
for name in names:
    print(name.lower())

# Print each name with index (starting from 1)
for i, name in enumerate(names, 1):
    print(f"{i} _ {name}")