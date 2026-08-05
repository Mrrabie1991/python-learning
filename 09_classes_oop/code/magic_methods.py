# 09_classes_oop/code/magic_methods.py
# Magic methods — like operator overloading in C++

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Like overriding operator<< or ToString()."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """For debugging — unambiguous representation."""
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """Overload + operator — like operator+ in C++."""
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """Overload == operator."""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Make the object work with len()."""
        return 2

    def __getitem__(self, index):
        """Make the object indexable — like operator[]."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

    def __call__(self, scalar):
        """Make the object callable like a function — operator()"""
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)                    # Vector(3, 4) — uses __str__
print(v1 + v2)               # Vector(4, 6) — uses __add__
print(v1 == v2)              # False — uses __eq__
print(len(v1))               # 2 — uses __len__
print(v1[0], v1[1])          # 3 4 — uses __getitem__

# Callable object
scaler = Vector(2, 3)
scaled = scaler(5)           # uses __call__ → Vector(10, 15)
print(scaled)                # Vector(10, 15)