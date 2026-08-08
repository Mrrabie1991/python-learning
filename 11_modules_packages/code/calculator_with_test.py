# calculator_with_test.py
# This file can be BOTH imported AND run directly

PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test code — only runs when file is executed directly
if __name__ == "__main__":
    print("Testing calculator module:")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"PI = {PI}")