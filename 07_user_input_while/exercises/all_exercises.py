# 07_user_input_while/exercises/all_exercises.py
# Chapter 07 Exercises — User Input & while Loops

# ============================================================
# Exercise 7.1: Sum of Numbers
# Get numbers from user until 0 is entered. Print total sum.
# ============================================================

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

print(f"Total sum: {total}")

print("\n","="*40,"\n")


# ============================================================
# Exercise 7.2: Guess the Number
# User guesses a fixed number. Get hints until correct.
# ============================================================

secret = 7

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret:
        print("Congratulations! You guessed it!")
        break
    elif guess < secret:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

print("\n","="*40,"\n")


# ============================================================
# Exercise 7.3: Input Validation
# Keep asking until user enters a valid number.
# ============================================================

while True:
    user_input = input("Enter a number: ")

    try:
        value = int(user_input)
        print(f"Valid number: {value}")
        break
    except ValueError:
        print("That's not a number. Please try again.")

print("\n","="*40,"\n")


# ============================================================
# Exercise 7.4: Collecting Items
# Collect items until user types 'done'. Print with numbering.
# ============================================================

items = []

print("Enter items one by one. Type 'done' to finish.")

while True:
    item = input("Item: ")

    if item.lower() == "done":
        break

    items.append(item)

print("\nYour items:")
for i, item in enumerate(items, 1):
    print(f"  {i}. {item}")

print("\n","="*40,"\n")


# ============================================================
# Exercise 7.5: Interactive Menu
# Menu with 3 options: add name, show list, exit.
# ============================================================

names = []


def add_name():
    """Add names until user returns to main menu."""
    while True:
        name = input("Enter a name (or 'back' to return to menu): ")

        if name.lower() == "back":
            return

        names.append(name)
        print(f"Added: {name}")


def show_names():
    """Display all names."""
    if not names:
        print("List is empty.")
        return

    print("Names:")
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name}")


while True:
    print("\n--- Menu ---")
    print("1. Add name")
    print("2. Show names")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_name()
    elif choice == "2":
        show_names()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")