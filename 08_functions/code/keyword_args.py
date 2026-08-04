# 08_functions/code/keyword_args.py
# Keyword arguments — passing by name, not position

def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old, lives in {city}")

# Positional arguments (like C++)
describe_person("Ali", 25, "Tehran")

# Keyword arguments — order doesn't matter
describe_person(age=30, name="Sara", city="Isfahan")

# Mix — positional first, then keyword
describe_person("Reza", city="Shiraz", age=22)