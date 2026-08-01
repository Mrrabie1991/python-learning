# 07_user_input_while/code/while_with_lists.py
# Common patterns: while with lists

# ---- Collecting items until sentinel ----
items = []
print("Enter items one by one. Enter 'done' to finish.")

while True:
    item = input("Item: ")
    if item.lower() == "done":
        break
    items.append(item)

print(f"\nYou entered {len(items)} items:")
for i, item in enumerate(items, 1):  # enumerate starting from 1
    print(f"  {i}. {item}")

# ---- Removing items from list while iterating ----
# Safe way: use while with condition (not for loop)
numbers = [1, 2, 2, 3, 2, 4]
while 2 in numbers:
    numbers.remove(2)  # Remove one occurrence at a time
print(f"After removing all 2s: {numbers}")  # [1, 3, 4]

# Why not for loop? Modifying list while iterating skips elements:
numbers = [1, 2, 2, 3, 2, 4]
for n in numbers:
    if n == 2:
        numbers.remove(n)  # DANGER: skips next element
print(f"Buggy result: {numbers}")  # [1, 2, 3, 4] — one '2' remains!