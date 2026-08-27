# Exercise 3.5: Matrix with List Comprehension
# Requirements:
# - Create 3x3 matrix with list comprehension
# - Print all elements
# - Print main diagonal
# - Print transpose (hint: zip(*matrix))

# Create 3x3 matrix with list comprehension
matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print all elements
print("Matrix:")
for row in matrix:
    print(*row)  # Unpack each row 

# Print main diagonal
print("\nMain diagonal:")
diagonal = [matrix[i][i] for i in range(3)]
print(diagonal)  # [1, 5, 9]

# Print transpose
print("\nTranspose:")
transpose = [list(row) for row in zip(*matrix)]
print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]