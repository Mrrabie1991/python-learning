# 07_user_input_while/code/input_validation.py
# Standard input validation pattern in Python

# Validate numeric range
while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        break
    print("Out of range. Try again.")

print(f"Valid input: {num}")