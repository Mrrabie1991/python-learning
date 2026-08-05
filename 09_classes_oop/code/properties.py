# 09_classes_oop/code/properties.py
# @property — Pythonic getter/setter

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # "private" attribute

    @property
    def age(self):
        """Getter — like get_age() in C++."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter — like set_age() in C++."""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property
    def is_adult(self):
        """Computed property — no setter needed."""
        return self._age >= 18

ali = Person("Ali", 25)
print(ali.age)       # 25 — looks like direct access, but calls getter
ali.age = 30         # Calls setter — with validation
# ali.age = -5       # ValueError: Age cannot be negative
print(ali.is_adult)  # True — computed property