# 09_classes_oop/code/inheritance.py
# Inheritance — Python vs C++

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """To be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement speak()")

class Dog(Animal):  # class Dog : public Animal in C++
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):  # class Cat : public Animal in C++
    def speak(self):
        return f"{self.name} says Meow!"

# Multiple inheritance — Python supports it, C++ too (with care)
class Pet:
    def play(self):
        return f"{self.name} is playing"

class Puppy(Dog, Pet):  # Multiple inheritance
    pass

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]

for animal in animals:
    print(animal.speak())
    # Rex says Woof!
    # Whiskers says Meow!
    # Buddy says Woof!

puppy = Puppy("Max")
print(puppy.speak())  # Max says Woof! (from Dog)
print(puppy.play())   # Max is playing (from Pet)