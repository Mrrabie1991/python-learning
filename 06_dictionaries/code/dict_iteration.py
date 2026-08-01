# 06_dictionaries/code/dict_iteration.py
# Iterating over dicts

person = {"name": "Ali", "age": 25, "city": "Tehran"}

# Loop over keys (default)
for key in person:
    print(key)

# Loop over keys explicitly
for key in person.keys():
    print(f"Key: {key}")

# Loop over values
for value in person.values():
    print(f"Value: {value}")

# Loop over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")