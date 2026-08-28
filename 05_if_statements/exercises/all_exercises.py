# 05_if_statements/exercises/all_exercises.py
# Chapter 05 Exercises — if Statements

# ============================================================
# Exercise 5.1: Simple Condition
# Get a number from user. Print "Positive", "Negative", or "Zero".
# ============================================================

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("\n","="*20,"\n")


# ============================================================
# Exercise 5.2: Grading
# Get a score from user. Convert to letter grade.
# ============================================================

score = int(input("Enter a score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# Same logic with match-case
match score:
    case s if s >= 90:
        grade_match = "A"
    case s if s >= 80:
        grade_match = "B"
    case s if s >= 70:
        grade_match = "C"
    case s if s >= 60:
        grade_match = "D"
    case _:
        grade_match = "F"

print(f"Grade (match): {grade_match}")

print("\n","="*20,"\n")


# ============================================================
# Exercise 5.3: Truthy/Falsy Check
# Get input from user. Check if empty or not.
# ============================================================

user_input = input("Enter something: ")

if not user_input:  # Empty string is falsy
    print("Empty input")
else:
    print(f"Input length: {len(user_input)}")

print("\n","="*20,"\n")


# ============================================================
# Exercise 5.4: Ternary Operator
# Get a number. Print "Even"/"Odd" and "Positive"/"Non-positive".
# ============================================================

num2 = int(input("Enter a number: "))

parity = "Even" if num2 % 2 == 0 else "Odd"
sign = "Positive" if num2 > 0 else "Non-positive"

print(f"Parity: {parity}")
print(f"Sign: {sign}")

print("\n","="*20,"\n")


# ============================================================
# Exercise 5.5: Leap Year
# Get a year. Check if leap year.
# Rules:
#   - Divisible by 4 → leap year
#   - Unless divisible by 100 → not leap year
#   - Unless divisible by 400 → leap year
# ============================================================

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")