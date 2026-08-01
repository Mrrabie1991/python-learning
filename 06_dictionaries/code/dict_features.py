# 06_dictionaries/code/dict_features.py
# Key dict features

# ---- Keys must be immutable ----
# Valid keys: str, int, float, bool, tuple (if all elements are immutable)
valid = {
    42: "int key",
    3.14: "float key",
    (1, 2): "tuple key"
}
print(f"Valid keys: {valid}")

# Invalid key — list is mutable
# invalid = {[1, 2]: "list key"}  # TypeError: unhashable type: 'list'

# ---- dict comprehension — like list comprehension ----
squares = {x: x * x for x in range(1, 6)}
print(f"Squares dict: {squares}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ---- Merging dicts (Python 3.9+) ----
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2  # like set union — d2 overwrites d1
print(f"Merged: {merged}")  # {'a': 1, 'b': 3, 'c': 4}

# ---- Creating dict from keys with default value ----
keys = ["a", "b", "c"]
default = dict.fromkeys(keys, 0)
print(f"From keys: {default}")  # {'a': 0, 'b': 0, 'c': 0}