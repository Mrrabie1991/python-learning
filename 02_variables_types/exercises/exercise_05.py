# 02_variables_types/exercises/exercise_05.py

# Small integers (1-9) — cached by Python
small_list = [i for i in range(1, 10)]

print("Small integers (cached):")
for i in small_list:
    print(id(i))
    # 140718998799480
    # 140718998799512
    # ...
    # These IDs are FIXED across runs — Python caches -5 to 256

# Large integers (1000-1008) — not cached
big_list = [i for i in range(1000, 1009)]

print("\nLarge integers (not cached):")
for i in big_list:
    print(id(i))
    # 2309365161008
    # 2309365161168
    # ...
    # These IDs CHANGE across runs — new objects created each time