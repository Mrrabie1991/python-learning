# 10_files_exceptions/code/raising_exceptions.py
# raise — like 'throw' in C++

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError(f"Age {age} is unrealistic")
    print(f"Age set to {age}")

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")  # Error: Age 200 is unrealistic