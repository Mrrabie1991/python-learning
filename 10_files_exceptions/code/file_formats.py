# 10_files_exceptions/code/file_formats.py
# Working with CSV and JSON files

import csv
import json

# ---- CSV ----
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ali", "25", "Tehran"])
    writer.writerow(["Sara", "30", "Isfahan"])

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']}, lives in {row['City']}")

# ---- JSON ----
data = {
    "name": "Ali",
    "age": 25,
    "skills": ["Python", "C++"],
}

# Write JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Read JSON
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(f"\nLoaded from JSON: {loaded}")
    print(f"Type: {type(loaded)}")  # <class 'dict'>