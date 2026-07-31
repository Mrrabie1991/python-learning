# 04_working_with_lists/code/while_loop.py
# while loop and loop control

# ---- while loop ----
count = 0
while count < 5:
    print(count)
    count += 1

# ---- break — exit the loop ----
for n in range(10):
    if n == 5:
        break
    print(n)  # 0, 1, 2, 3, 4

# ---- continue — skip to the next iteration ----
for n in range(5):
    if n == 2:
        continue
    print(n)  # 0, 1, 3, 4