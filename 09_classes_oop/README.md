# 09 - Classes & OOP (Pythonic)

## Class Definition — Comparison with C++

In Python, classes are defined with the `class` keyword. Unlike C++, there is no semicolon at the end of the class definition and no mandatory access modifiers. All methods must accept `self` as their first parameter — `self` is equivalent to `this` in C++, except it is written explicitly.

**Applications in Intelligent Systems:** Classes are the primary units for modeling system entities — from sensors and actuators to data processing algorithms and decision-making agents. Proper class design enables maintenance and extension of complex systems.

```python
# C++:
# class Person {
# private:
#     string name;
#     int age;
# public:
#     Person(string n, int a) : name(n), age(a) {}
#     void greet() { cout << "Hello, I'm " << name << endl; }
# };

class Person:
    """A simple Person class."""

    def __init__(self, name, age):
        """Constructor — like Person(string n, int a) in C++."""
        self.name = name  # self = this in C++
        self.age = age

    def greet(self):
        """Method — like void greet() in C++."""
        print(f"Hello, I'm {self.name}, {self.age} years old")

# Creating instances — no 'new' keyword
ali = Person("Ali", 25)
ali.greet()  # Hello, I'm Ali, 25 years old
```

### General Comparison

| Concept | C++ | Python |
|---|---|---|
| Class definition | `class Person { };` | `class Person:` |
| Constructor | `Person(string n, int a)` | `def __init__(self, name, age):` |
| Destructor | `~Person()` | `def __del__(self):` (rare — GC is sufficient) |
| Self-reference | `this->name` (implicit `this`) | `self.name` (explicit `self`, first parameter) |
| Instantiation | `Person ali("Ali", 25);` | `ali = Person("Ali", 25)` |
| Access modifiers | `private`, `public`, `protected` | None — naming convention (`_`, `__`) |

---

## `self` — Equivalent to `this` in C++

`self` in Python is exactly like `this` in C++ — it refers to the current instance. Three key differences:

1. `self` must be **explicitly** written as the first parameter of every method (in C++, `this` is implicit).
2. Accessing attributes always requires `self.` (in C++, `this->` is often optional).
3. The name `self` is convention — another name could be used, but this is never recommended.

```python
class Counter:
    def __init__(self):
        self.count = 0  # self.count — instance attribute

    def increment(self):
        self.count += 1  # C++: ++this->count (this-> is optional)
        return self.count
```

---

## Constructor — `__init__`

`__init__` is Python's constructor. Key differences from C++:

- **Can create new attributes on the fly** — no prior declaration needed.
- **Only one `__init__` can exist** — Python has no function overloading.
- **To simulate overloading**, use default arguments or `@classmethod`.

```python
class Point:
    def __init__(self, x=0, y=0):  # Default arguments — simulates overloading
        """Create a Point. If no args, defaults to (0, 0)."""
        self.x = x
        self.y = y

# Multiple ways to create — like function overloading
p1 = Point()         # (0, 0)
p2 = Point(3)        # (3, 0)
p3 = Point(3, 4)     # (3, 4)
```

---

## Attributes — Public and "Private"

Python has no access modifiers (like `private` and `public`). Instead, a **naming convention** is used:

- `name` — public (anyone can read and modify)
- `_name` — "protected" (convention: please don't touch from outside)
- `__name` — name mangling (Python renames to `_ClassName__name` to prevent accidental access — not truly private)

```python
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
```

**Python's Philosophy:** "We are all consenting adults here." — Trust the programmer. If someone wants to access `_method`, they bear the responsibility.

---

## Property — Pythonic Getter/Setter

In C++, encapsulation uses getter/setter methods. In Python, `@property` does this more Pythonically:

```python
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
        """Setter — like set_age() in C++ with validation."""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property
    def is_adult(self):
        """Computed property — no setter needed."""
        return self._age >= 18

ali = Person("Ali", 25)
print(ali.age)       # 25 — instead of ali.get_age()
ali.age = 30         # instead of ali.set_age(30) — with validation
print(ali.is_adult)  # True — computed property, no parentheses
```

**Why `@property` is Pythonic:**
- Readability: `ali.age = 30` is more natural than `ali.set_age(30)`.
- Can add getter/setter later without changing external code.
- Computed properties accessible without parentheses.

---

## Magic Methods (Dunder Methods)

Python has special methods that start and end with `__`. These define how objects interact with operators and built-in functions — equivalent to operator overloading in C++.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Like operator<< or ToString() in C++."""
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
        raise IndexError("Vector index out of range")

    def __call__(self, scalar):
        """Make the object callable — like operator() in C++."""
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)              # Vector(3, 4) — uses __str__
print(v1 + v2)         # Vector(4, 6) — uses __add__
print(v1 == v2)        # False — uses __eq__
print(len(v1))         # 2 — uses __len__
print(v1[0], v1[1])    # 3 4 — uses __getitem__

scaler = Vector(2, 3)
scaled = scaler(5)     # uses __call__ → Vector(10, 15)
```

### Common Magic Methods

| Magic Method | Operator/Function | C++ Equivalent |
|---|---|---|
| `__init__` | Constructor | `ClassName(...)` |
| `__del__` | Destructor | `~ClassName()` |
| `__str__` | `print(obj)`, `str(obj)` | `operator<<` or `ToString()` |
| `__repr__` | `repr(obj)` | Debug output |
| `__add__` | `+` | `operator+` |
| `__eq__` | `==` | `operator==` |
| `__len__` | `len(obj)` | `size()` |
| `__getitem__` | `obj[index]` | `operator[]` |
| `__call__` | `obj(args)` | `operator()` |

---

## Class Method and Static Method

Python has no function overloading, so multiple constructors with different signatures are not possible. `@classmethod` solves this by providing **alternative constructors (Factory Methods)**.

### `@classmethod` — Alternative Constructor

`cls` (the first parameter) refers to the class itself — like `self` refers to the instance. The key advantage: in inheritance, `cls` refers to the subclass, not the parent.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Factory method — alternative constructor."""
        age = 2026 - birth_year
        return cls(name, age)  # cls = Person (or subclass)

    @classmethod
    def from_json(cls, json_string):
        """Another constructor — from JSON."""
        import json
        data = json.loads(json_string)
        return cls(data["name"], data["age"])

# Three ways to create a Person
p1 = Person("Ali", 25)
p2 = Person.from_birth_year("Sara", 1990)
p3 = Person.from_json('{"name":"Reza","age":22}')

# In inheritance, cls refers to the subclass
class Employee(Person):
    pass

e = Employee.from_birth_year("Ali", 1990)
print(type(e))  # <class 'Employee'> — not Person!
```

### `@staticmethod` — Utility Function Related to the Class

A regular function logically related to the class, but needs neither `self` nor `cls`. Like a function you could write outside the class, but placed inside for better organization.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

# Usable without creating an instance
print(Math.add(3, 5))    # 8
print(Math.is_even(10))  # True
```

### Method Type Comparison

| Method Type | First Parameter | Access To | Primary Use | C++ Equivalent |
|---|---|---|---|---|
| Instance | `self` (instance) | `self.attr` | Working with instance data | Regular method |
| Class | `cls` (class) | `cls.attr`, the class | Alternative constructor, factory | `static` with template |
| Static | None | None | Class-related utility functions | `static` |

---

## Inheritance

Python supports single and multiple inheritance. Unlike C++, all methods are automatically **virtual** — no `virtual` keyword needed.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """To be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement speak()")

class Dog(Animal):  # class Dog : public Animal in C++
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Multiple inheritance
class Pet:
    def play(self):
        return f"{self.name} is playing"

class Puppy(Dog, Pet):  # Multiple inheritance
    pass

animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  # Polymorphism — like virtual functions

puppy = Puppy("Max")
print(puppy.speak())  # Max says Woof! (from Dog)
print(puppy.play())   # Max is playing (from Pet)
```

### Inheritance Comparison

| Concept | C++ | Python |
|---|---|---|
| Single inheritance | `class Dog : public Animal { };` | `class Dog(Animal):` |
| Multiple inheritance | `class C : public A, public B { };` | `class C(A, B):` |
| Virtual method | `virtual void speak();` | All methods are virtual |
| Pure virtual | `virtual void speak() = 0;` | `raise NotImplementedError` |
| Parent constructor | `Animal(name)` in initializer list | `super().__init__(name)` |
| Virtual destructor | Needs `virtual ~Base()` | Not needed — GC handles it |

---

## Duck Typing — Polymorphism Without Inheritance

In C++, polymorphism is achieved through inheritance + virtual functions. In Python, **Duck Typing** is the primary alternative: "If it walks like a duck and quacks like a duck, it's a duck."

This eliminates the need for a common base class and greatly increases flexibility.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:  # Inherits from nothing
    def speak(self):
        return "Quack!"

def make_it_speak(thing):
    """Any object with speak() works — no common base class needed."""
    return thing.speak()

print(make_it_speak(Dog()))   # Woof!
print(make_it_speak(Cat()))   # Meow!
print(make_it_speak(Duck()))  # Quack!
```

**Application in Intelligent Systems:** Different sensors (`CameraSensor`, `LidarSensor`, `TemperatureSensor`) each have `read()`. With Duck Typing, all can be processed uniformly without needing a `SensorBase` class.

```python
def collect_data(sensor):
    return sensor.read()  # Any sensor with read() works

# All work — even from completely different libraries
data = collect_data(camera)       # From library A
data = collect_data(lidar)        # From library B
data = collect_data(temperature)  # From library C
```

---

## The Four OOP Principles in Python

### 1. Encapsulation

Data and related methods are bundled in a class. Access to internal data is controlled through the `_` and `__` convention and `@property` — not by compiler enforcement, but by trusting the programmer.

### 2. Abstraction

Internal complexity is hidden and only a simple interface is exposed. In Python, this is achieved with Duck Typing (any object with the required method) or `ABC` + `@abstractmethod`.

### 3. Inheritance

Child classes inherit attributes and behaviors from parent classes. In Python, Composition (using an object as an attribute) is often preferred over Inheritance — more flexibility, less coupling.

### 4. Polymorphism

Different objects respond to the same message (method) in different ways. In Python, Duck Typing is the primary method of polymorphism — no inheritance or virtual functions required.

---

## Abstract Base Classes — The `abc` Module

If you want to **force** subclasses to implement specific methods, use `ABC` and `@abstractmethod`. This is similar to pure virtual functions in C++.

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    """Cannot be instantiated directly."""

    @abstractmethod
    def area(self):
        """Must be overridden by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """Must be overridden by subclasses."""
        pass

    def describe(self):
        """Concrete method — inherited as-is."""
        return f"Shape with area={self.area()}, perimeter={self.perimeter()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# s = Shape()  # TypeError — cannot instantiate abstract class
c = Circle(5)
print(c.describe())  # Shape with area=78.53975, perimeter=31.4159
```

### Abstract Class Comparison

| Concept | C++ | Python |
|---|---|---|
| Definition | `class Shape { virtual double area() = 0; };` | `class Shape(ABC): @abstractmethod` |
| Pure virtual | `= 0;` | `@abstractmethod` |
| Prevent instantiation | Yes — compile error | Yes — TypeError at runtime |
| Virtual destructor | Needed | Not needed |

---

## Dataclass — Simple Data Classes (Python 3.7+)

`dataclass` automatically generates `__init__`, `__repr__`, `__eq__`, and other methods. Equivalent to `struct` in C++.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1)           # Point(x=3, y=4) — auto-generated __repr__
print(p1 == p2)     # True — auto-generated __eq__
```

---

## `__slots__` — Memory Optimization

Every Python instance has a `__dict__` to store attributes, which creates memory overhead. `__slots__` removes this `__dict__` and only allows the specified attributes. Suitable when creating millions of instances of a class.

```python
class Point:
    __slots__ = ("x", "y")  # No new attributes can be added

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
# p.z = 5  # AttributeError — only x and y allowed
```

---

## Composition over Inheritance

In Python, due to Duck Typing, **Composition** (using another object as an attribute) is often preferred over **Inheritance**. This reduces coupling and increases flexibility.

```python
# Inheritance — rigid hierarchy
class Robot:
    def move(self):
        pass

class FlyingRobot(Robot):
    def fly(self):
        pass

# Composition — more flexible
class FlyBehavior:
    def fly(self):
        return "Flying"

class Robot:
    def __init__(self, behavior):
        self.behavior = behavior  # Behavior as an attribute

    def perform_action(self):
        return self.behavior.fly()  # Any behavior with fly() works

robot = Robot(FlyBehavior())
print(robot.perform_action())  # Flying
```

---

## Key Takeaways

1. **Classes are defined with `class` and `self` is the explicit equivalent of C++'s `this`.** Writing `self` as the first parameter of all instance methods is mandatory.

2. **Python has no mandatory access modifiers.** The `_` (protected) and `__` (name mangling) convention is used. Philosophy: "We are all consenting adults."

3. **`@property` is the Pythonic replacement for getter/setter.** Higher readability, ability to add validation without changing external code, and computed properties without parentheses.

4. **Python has no function overloading.** This is compensated with default arguments and `@classmethod` (alternative constructors).

5. **`@classmethod` is used for factory methods.** `cls` refers to the class (or subclass in inheritance). `@staticmethod` is for utility functions that need neither `self` nor `cls`.

6. **All methods are virtual.** Polymorphism is automatic — no `virtual` or `override` keywords needed.

7. **Duck Typing is the primary method of polymorphism in Python.** "If it walks like a duck, it's a duck." Any object with the required method can be used — no common base class needed.

8. **Abstract Base Classes (`abc`) are used to force subclasses to implement methods.** Equivalent to pure virtual functions in C++.

9. **`dataclass` is the Python equivalent of C++'s `struct`.** Auto-generates `__init__`, `__repr__`, `__eq__`.

10. **`__slots__` optimizes memory for classes with many instances.** But removes the flexibility to add new attributes.

11. **Composition is preferred over Inheritance.** More flexibility, less coupling.

12. **Magic Methods (Dunder Methods) are the Python equivalent of C++ operator overloading.** `__add__` for `+`, `__eq__` for `==`, `__call__` for `operator()`, etc.

13. **Functions in Python are themselves objects.** Mutable default arguments are created only once at `def` time (from Chapter 08).

---

## Q&A / Key Insights

### Q: What are `@classmethod` and `@staticmethod` used for, and how do they differ?
**A:** `@classmethod` is used to create alternative constructors (factory methods) — `cls` refers to the class and, in inheritance, reflects the actual subclass type. `@staticmethod` is a regular function placed inside a class for better organization — it has neither `self` nor `cls`. In C++, `@staticmethod` has a direct `static` equivalent, but `@classmethod` has no direct counterpart.

### Q: What problem does Duck Typing solve?
**A:** It eliminates the need for a common base class. In C++, to process different objects uniformly, you either need inheritance (which creates coupling) or templates (checked at compile time). Duck Typing in Python allows any object with the required method to be used — even from completely different libraries.

### Q: How are the four OOP principles implemented in Python?
**A:** Encapsulation via `_` convention and `@property` (not compiler enforcement). Abstraction via Duck Typing or `ABC`. Inheritance via `class D(B):` but Composition is often preferred. Polymorphism primarily via Duck Typing — no inheritance or virtual functions required.

### Q: When should Abstract Base Classes be used?
**A:** When you want to **force** subclasses to implement specific methods. Like pure virtual functions in C++. If this enforcement is not needed, Duck Typing is sufficient and more Pythonic.

### Q: Why doesn't Python have true `private`?
**A:** Python's philosophy is "We are all consenting adults" — it trusts the programmer. `__` (name mangling) is designed to prevent name collisions in inheritance, not for security. This philosophy accepts flexibility at the cost of some compile-time guarantees.