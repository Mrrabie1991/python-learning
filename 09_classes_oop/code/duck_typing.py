# 09_classes_oop/code/duck_typing.py
# Duck Typing — polymorphism without inheritance

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Car:
    def horn(self):
        return "Beep!"

class Duck:
    def speak(self):
        return "Quack!"

# Any object with speak() works — no common base class needed
def make_it_speak(thing):
    """Call speak() on any object that has it."""
    return thing.speak()

print(make_it_speak(Dog()))   # Woof!
print(make_it_speak(Cat()))   # Meow!
print(make_it_speak(Duck()))  # Quack!
# print(make_it_speak(Car())) # AttributeError — Car has no speak()