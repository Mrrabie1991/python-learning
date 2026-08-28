# Exercise 4.5: Simple Data Analysis

scores = [85, 92, 78, 95, 88, 76, 90]

# Scores above 80
above_80 = [i for i in scores if i > 80]
print(f"Scores above 80: {above_80}")

# Average
average = sum(scores) / len(scores)
print(f"Average: {average}")

# Print each score with rank (rank from 1)
scores_sorted = sorted(scores, reverse=True)
for rank, score in enumerate(scores_sorted, 1):
    print(f"Rank {rank}: {score}")

# Find max without max() — using loop
max_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score
print(f"Max: {max_score}")

# Find min without min() — using loop
min_score = scores[0]
for score in scores:
    if score < min_score:
        min_score = score
print(f"Min: {min_score}")