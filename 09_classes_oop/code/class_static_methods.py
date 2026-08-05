# 09_classes_oop/code/class_static_methods.py
# @classmethod and @staticmethod

class Person:
    species = "Homo sapiens"  # Class attribute — like static member

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method — receives self (the instance)
    def greet(self):
        print(f"Hi, I'm {self.name}")

    # Class method — receives cls (the class itself)
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Factory method — alternative constructor."""
        from datetime import date
        age = date.today().year - birth_year
        return cls(name, age)  # cls() = Person()

    # Static method — receives nothing (like regular function)
    @staticmethod
    def is_valid_age(age):
        """Utility function related to Person."""
        return 0 <= age <= 150

# Using factory method
ali = Person.from_birth_year("Ali", 1990)
print(f"{ali.name} is {ali.age}")  # Ali is 36 (or current year - 1990)

# Using static method
print(Person.is_valid_age(25))   # True
print(Person.is_valid_age(200))  # False

# Class attribute
print(Person.species)  # Homo sapiens