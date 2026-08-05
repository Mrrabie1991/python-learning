# 09_classes_oop/code/class_basics.py
# Class definition in Python vs C++

class Person:
    """A simple Person class."""

    def __init__(self, name, age):
        """Constructor — like Person(string n, int a) in C++."""
        self.name = name  # self = this in C++
        self.age = age

    def greet(self):
        """Method — like void greet() in C++."""
        print(f"Hello, I'm {self.name}, {self.age} years old")

    def have_birthday(self):
        """Modify object state."""
        self.age += 1
        print(f"Happy birthday! Now {self.age}")

# Creating instances — no 'new' keyword
ali = Person("Ali", 25)
sara = Person("Sara", 30)

ali.greet()           # Hello, I'm Ali, 25 years old
sara.greet()          # Hello, I'm Sara, 30 years old
ali.have_birthday()   # Happy birthday! Now 26

#*************************************************************

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # public
        self._bank = "MyBank"     # "protected" — convention
        self.__balance = balance  # name mangling

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Ali", 1000)
print(acc.owner)        # Ali — OK
print(acc._bank)        # MyBank — works, but against convention
# print(acc.__balance)  # AttributeError!
print(acc._BankAccount__balance)  # 1000 — name mangling can be bypassed