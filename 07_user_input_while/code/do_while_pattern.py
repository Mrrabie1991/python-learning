# 07_user_input_while/code/do_while_pattern.py
# do-while pattern in Python — while True + break

# C++ do-while:
# do {
#     x = get_input();
# } while (x < 0);

# Python equivalent — while True + break
while True:
    x = int(input("Enter a positive number: "))
    if x > 0:
        break
    print("That's not positive. Try again.")

print(f"You entered: {x}")