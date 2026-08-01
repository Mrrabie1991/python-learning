# 06_dictionaries/code/dict_basics.py
# Python dict — like std::unordered_map, built into the language

# ---- Creating dicts ----
# C++: std::unordered_map<std::string, int> ages = {{"Ali", 25}, {"Sara", 30}};
ages = {"Ali": 25, "Sara": 30, "Reza": 22}
empty = {}
print(f"ages: {ages}")

# ---- Accessing values by key ----
print(f"Ali's age: {ages['Ali']}")

# .get() — safe access (returns None or default if key doesn't exist)
print(f"Sara's age: {ages.get('Sara')}")
print(f"Unknown: {ages.get('Unknown')}")         # None — no error
print(f"Unknown: {ages.get('Unknown', 'N/A')}")  # 'N/A'

# ---- Adding and updating ----
ages["Maryam"] = 28       # Add new key-value pair
ages["Ali"] = 26           # Update existing value
print(f"Updated: {ages}")

# ---- Removing ----
del ages["Reza"]           # Remove by key
print(f"After del: {ages}")

popped = ages.pop("Sara")  # Remove and return value
print(f"Popped: {popped}, remaining: {ages}")

# ---- Checking key existence ----
print(f"'Ali' in ages: {'Ali' in ages}")
print(f"'Reza' in ages: {'Reza' in ages}")

# ---- Length ----
print(f"Number of entries: {len(ages)}")