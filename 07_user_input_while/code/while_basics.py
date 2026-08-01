# 07_user_input_while/code/while_basics.py
# while loop — identical logic to C++

# Simple counter
count = 0
while count < 5:
    print(count)
    count += 1

# while with user input — sentinel pattern
message = ""
while message != "quit":
    message = input("Enter a message (or 'quit' to exit): ")
    if message != "quit":
        print(f"You entered: {message}")