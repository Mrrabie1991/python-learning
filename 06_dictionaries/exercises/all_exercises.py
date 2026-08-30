# 06_dictionaries/exercises/all_exercises.py
# Chapter 06 Exercises — Dictionaries

# ============================================================
# Exercise 6.1: Creating and Accessing a Dict
# ============================================================

person = {"name": "Ali", "age": 25, "city": "Tehran"}

print(person["name"])                      # Direct access
print(person.get("age"))                   # Safe access
print(person.get("country", "Iran"))       # Safe access with default

print("\n","="*20,"\n")


# ============================================================
# Exercise 6.2: Adding, Modifying, Removing
# ============================================================

data = {}

# Adding key-value pairs
data["name"] = "Sara"
data["age"] = 30
data["city"] = "Isfahan"

# Modifying a value
data["age"] = 31

# Removing with del
del data["city"]

# Removing with pop (returns the value)
popped = data.pop("age")
print(f"Popped value: {popped}")

print(f"Final dict: {data}")

print("\n","="*20,"\n")


# ============================================================
# Exercise 6.3: Iterating over a Dict
# ============================================================

scores = {"Ali": 85, "Sara": 92, "Reza": 78}

# Keys only
print("Keys:")
for key in scores:
    print(f"  {key}")

# Values only
print("Values:")
for value in scores.values():
    print(f"  {value}")

# Key-value pairs
print("Key-Value pairs:")
for key, value in scores.items():
    print(f"  {key}: {value}")

# Average
average = sum(scores.values()) / len(scores)
print(f"Average: {average}")

print("\n","="*20,"\n")


# ============================================================
# Exercise 6.4: Dict Comprehension
# ============================================================

# Squares of numbers 1 to 5
squares = {x: x * x for x in range(1, 6)}
print(f"Squares: {squares}")

# Filter scores above 80
high_scores = {k: v for k, v in scores.items() if v > 80}
print(f"High scores: {high_scores}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

print("\n","="*20,"\n")


# ============================================================
# Exercise 6.5: Word Counter
# ============================================================

text = "the cat and the dog and the bird"

words = text.split()
word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word counts:")
for word, count in word_count.items():
    print(f"  {word}: {count}")