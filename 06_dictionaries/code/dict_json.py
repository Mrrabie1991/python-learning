# 06_dictionaries/code/dict_json.py
# dict and JSON — nearly identical in Python

import json

# dict — Python object
person = {
    "name": "Ali",
    "age": 25,
    "skills": ["Python", "C++"],
    "address": {
        "city": "Tehran",
        "country": "Iran"
    }
}

# Convert dict to JSON string
json_string = json.dumps(person, indent=2, ensure_ascii=False)
print(f"JSON:\n{json_string}")

# Convert JSON string back to dict
json_data = '{"name": "Sara", "age": 30}'
parsed = json.loads(json_data)
print(f"Parsed: {parsed}")
print(f"Type: {type(parsed)}")  # <class 'dict'>