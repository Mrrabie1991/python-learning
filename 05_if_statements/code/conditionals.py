# 05_if_statements/code/conditionals.py
# Python conditionals — if, elif, else

x = 10

# if
if x > 5:
    print("x is greater than 5")

# if-else
if x > 20:
    print("x is greater than 20")
else:
    print("x is not greater than 20")

# if-elif-else (equivalent to else if in C++)
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")