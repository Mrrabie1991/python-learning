# 10_files_exceptions/code/file_basics.py
# Reading and writing files in Python

# ---- Writing to a file ----
# C++: ofstream file("output.txt"); file << "Hello";
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("This is line 2.\n")

print("File written.")

# ---- Reading entire file ----
with open("output.txt", "r", encoding="utf-8") as file:
    content = file.read()  # Read all at once
    print("Entire file:")
    print(content)

# ---- Reading line by line ----
with open("output.txt", "r", encoding="utf-8") as file:
    print("Line by line:")
    for line in file:
        print(f"  {line.strip()}")  # strip() removes \n

# ---- Reading all lines into a list ----
with open("output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(f"Lines as list: {lines}")