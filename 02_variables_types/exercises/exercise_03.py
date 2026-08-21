# 02_variables_types/exercises/exercise_03.py

# Attempt to modify an int — should fail (immutable)
try:
    x = 5
    x[0] = 3
except Exception as e:
    print(f"Exception : {e}")

# Attempt to modify a str — should fail (immutable)
try:
    s = "Hello"
    s[0] = "h"
except Exception as e:
    print(f"Exception : {e}")

# Show that x = 5 and x = 6 are different objects
x = 5
print(f"id of x = 5 : {id(x)}")

x = 6
print(f"id of x = 6 : {id(x)}")