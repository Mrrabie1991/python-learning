# 07_user_input_while/code/user_input.py
# input() always returns str — like std::getline in C++

# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# input returns str — must convert for numbers
# C++: int age = std::stoi(input);
age_str = input("Enter your age: ")
age = int(age_str)
print(f"Next year you will be {age + 1}")

# One-liner conversion
height = float(input("Enter your height (m): "))
print(f"Your height is {height} meters")