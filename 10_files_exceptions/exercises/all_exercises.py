# 10_files_exceptions/exercises/all_exercises.py
# Chapter 10 Exercises — Files & Exceptions

# ============================================================
# Exercise 10.1: Write and Read a File
# Create test.txt, write three lines, read and print content.
# ============================================================

with open("test.txt", "w", encoding="utf-8") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("File content:")
print(content)

print("\n", "=" * 40, "\n")


# ============================================================
# Exercise 10.2: Read Line by Line
# Read test.txt line by line and print each with number.
# ============================================================

with open("test.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file, 1):
        print(f"{i}. {line.strip()}")

print("\n", "=" * 40, "\n")


# ============================================================
# Exercise 10.3: Error Handling
# Get filename from user. Read file. If not found, show error and retry.
# ============================================================

while True:
    filename = input("Enter filename to read: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"File content:\n{content}")
        break
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Try again.")

print("\n", "=" * 40, "\n")


# ============================================================
# Exercise 10.4: Read Numbers from File
# Create file with numbers, read and sum them, ignore non-numbers.
# ============================================================

# Create numbers.txt
with open("numbers.txt", "w", encoding="utf-8") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("thirty\n")  # Invalid — will be ignored
    file.write("40\n")
    file.write("50\n")

# Read and sum valid numbers
total = 0

with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        try:
            total += int(line.strip())
        except ValueError:
            print(f"Ignoring invalid line: '{line.strip()}'")

print(f"Total sum: {total}")

print("\n", "=" * 40, "\n")


# ============================================================
# Exercise 10.5: Simple CSV
# Create CSV file with 3 columns, write 3 rows, read as dict.
# ============================================================

import csv

# Write CSV
with open("people.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Ali", "25", "Tehran"])
    writer.writerow(["Sara", "30", "Isfahan"])
    writer.writerow(["Reza", "22", "Shiraz"])

# Read CSV as dict
with open("people.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} is {row['age']}, lives in {row['city']}")