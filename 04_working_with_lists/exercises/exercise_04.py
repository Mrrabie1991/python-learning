# Exercise 4.4: zip and enumerate

names = ["ali", "reza", "celin"]
scores = [15, 20, 18]

# Pair names with scores
names_and_scores = [i for i in zip(names, scores)]
print(names_and_scores)

# Print with index, name, and score
for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f"{i} - {name} - {score}")

# Zip with different lengths — shortest wins
names_long = ["ahmad", "sara", "mehdi", "narges", "ali", "reza", "maryam"]
scores_short = [85, 92, 78, 95, 88]

print(list(zip(names_long, scores_short)))