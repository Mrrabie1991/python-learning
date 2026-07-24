# 02_variables_types/code/variables_demo.py
# Demonstrating Python's Name Binding vs C++ Variable Assignment

# ---- Part 1: Dynamic Typing ----
# In C++: int x = 5;  // x is a box that holds an int
# In Python: x is a name that points to an int object

x = 5
print(f"x = {x}, type = {type(x)}, id = {id(x)}")

x = "Hello"  # x now points to a str object (impossible in C++)
print(f"x = {x}, type = {type(x)}, id = {id(x)}")

x = [1, 2, 3]  # x now points to a list object
print(f"x = {x}, type = {type(x)}, id = {id(x)}")

# ---- Part 2: int — arbitrary precision ----
# In C++: int is typically 4 bytes, limited range
# In Python: int has unlimited precision

big = 2 ** 100  # 2^100 — would overflow in C++ int
print(f"\n2^100 = {big}")
print(f"Digits in 2^100: {len(str(big))}")

# ---- Part 3: float — always double precision ----
# In C++: float (32-bit) and double (64-bit) are separate
# In Python: float is always 64-bit (like double)

pi = 3.141592653589793
print(f"\npi = {pi}")
print(f"pi type: {type(pi)}")

# ---- Part 4: str — immutable Unicode ----
# In C++: std::string is mutable, char[] for C-style
# In Python: str is immutable and Unicode by default

s = "Hello python"  # Unicode without any extra effort
print(f"\ns = {s}")
print(f"s[0] = {s[0]}")  # Indexing works
# s[0] = "h"  # ERROR — str is immutable
print(f"Length: {len(s)}")

# ---- Part 5: bool — subclass of int ----
# In C++: bool is a distinct type, true/false
# In Python: bool is a subclass of int, True/False (capitalized)

t = True
f = False
print(f"\nt = {t}, int(t) = {int(t)}")
print(f"f = {f}, int(f) = {int(f)}")
print(f"True + True = {True + True}")  # 2 — because bool is int

# ---- Part 6: None — the null object ----
# In C++: NULL, nullptr, or std::nullopt
# In Python: None is a singleton object of type NoneType

nothing = None
print(f"\nnothing = {nothing}, type = {type(nothing)}")
print(f"nothing is None: {nothing is None}")

# ---- Part 7: Type Conversion ----
# In C++: static_cast<int>(3.14), std::to_string(42)
# In Python: int(), float(), str()

num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print(f"\n'42' -> int: {num_int}, float: {num_float}")
print(f"str(100) + str(200) = {str(100) + str(200)}")  # "100200"
print(f"int(3.99) = {int(3.99)}")  # 3 — truncates, doesn't round