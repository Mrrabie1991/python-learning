# 09_classes_oop/exercises/exercises_01_to_04.py
# Chapter 09 Exercises 1-4 — Classes & OOP

# ============================================================
# Exercise 9.1: Simple Class
# ============================================================

class Car:
    """A simple car class."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


my_car = Car("Toyota", "Corolla")
my_car.start()
my_car.stop()

print("\n","="*40,"\n")


# ============================================================
# Exercise 9.2: Constructor and self
# ============================================================

class Person:
    """A simple person class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name}, {self.age} years old")


ali = Person("Ali", 25)
sara = Person("Sara", 30)

ali.greet()
sara.greet()

print("\n","="*40,"\n")


# ============================================================
# Exercise 9.3: Property
# ============================================================

class BankAccount:
    """Bank account with read-only balance."""

    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        """Add money to account."""
        if amount > 0:
            self._balance += amount

    @property
    def balance(self):
        """Read-only balance."""
        return self._balance

    @property
    def is_empty(self):
        """Check if balance is zero."""
        return self._balance == 0


account = BankAccount()
print(f"Initial balance: {account.balance}")
print(f"Is empty? {account.is_empty}")

account.deposit(500)
print(f"After deposit: {account.balance}")
print(f"Is empty? {account.is_empty}")

print("\n","="*40,"\n")


# ============================================================
# Exercise 9.4: Magic Methods
# ============================================================

class Point:
    """A 2D point with magic methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)               # Point(3, 4)
print(p1 + p2)          # Point(4, 6)
print(p1 == p2)         # False
print(p1 == Point(3, 4))  # True