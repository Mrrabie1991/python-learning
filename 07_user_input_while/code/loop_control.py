# 07_user_input_while/code/loop_control.py
# break and continue — same as C++

# break — exit loop immediately
for i in range(1, 10):
    if i == 5:
        break       # Exit loop when i == 5
    print(i)        # 1, 2, 3, 4

# continue — skip rest of current iteration
for i in range(1, 6):
    if i == 3:
        continue    # Skip print when i == 3
    print(i)        # 1, 2, 4, 5

# Practical example — sum numbers until 0
total = 0
while True:
    num = int(input("Number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Sum: {total}")