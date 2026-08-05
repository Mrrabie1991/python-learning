# ۰۹ - کلاس‌ها و شی‌گرایی (OOP)

## تعریف کلاس — مقایسه با C++

در پایتون، کلاس‌ها با کلمه کلیدی `class` تعریف می‌شوند. برخلاف C++، خبری از سمی‌کالن در انتهای تعریف کلاس و access modifierهای اجباری نیست. تمام متدها باید `self` را به‌عنوان اولین پارامتر دریافت کنند — `self` معادل `this` در C++ است با این تفاوت که صریحاً نوشته می‌شود.

**کاربرد در Intelligent Systems:** کلاس‌ها واحدهای اصلی مدل‌سازی موجودیت‌های سیستم هستند — از سنسورها و محرک‌ها گرفته تا الگوریتم‌های پردازش داده و عامل‌های تصمیم‌گیر. طراحی درست کلاس‌ها، نگهداری و گسترش سیستم‌های پیچیده را ممکن می‌سازد.

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

# ایجاد نمونه — بدون new
ali = Person("Ali", 25)
ali.greet()  # Hello, I'm Ali, 25 years old
```

### مقایسه کلی

| مفهوم | C++ | Python |
|---|---|---|
| تعریف کلاس | `class Person { };` | `class Person:` |
| Constructor | `Person(string n, int a)` | `def __init__(self, name, age):` |
| Destructor | `~Person()` | `def __del__(self):` (نادر — GC کافی است) |
| اشاره به خود | `this->name` (this ضمنی) | `self.name` (self صریح، اولین پارامتر) |
| ایجاد نمونه | `Person ali("Ali", 25);` | `ali = Person("Ali", 25)` |
| Access modifier | `private`, `public`, `protected` | ندارد — قرارداد نام‌گذاری (`_`, `__`) |

---

## [فارسی] `self` — معادل `this` در C++

[فارسی] `self` در پایتون دقیقاً مانند `this` در C++ است — اشاره به نمونه فعلی کلاس. سه تفاوت کلیدی:

۱. [فارسی] `self` باید **صراحتاً** به‌عنوان اولین پارامتر هر متد نوشته شود (در C++، `this` ضمنی است).

۲. برای دسترسی به attributeها همیشه باید `self.` نوشته شود (در C++، `this->` اغلب اختیاری است).

۳. نام `self` قراردادی است — می‌توان نام دیگری انتخاب کرد، اما این کار هرگز توصیه نمی‌شود.

```python
class Counter:
    def __init__(self):
        self.count = 0  # self.count — attribute نمونه

    def increment(self):
        self.count += 1  # در C++: ++this->count (this-> اختیاری)
        return self.count
```

---

## تابع Constructor سازنده  — `__init__`

در پایتون `__init__` تابع constructor پایتون است. تفاوت‌های کلیدی با C++:

- **می‌تواند attributeهای جدید را در لحظه ایجاد کند** — نیازی به تعریف قبلی نیست.
- **فقط یک `__init__` می‌تواند وجود داشته باشد** — پایتون function overloading ندارد.
- **برای شبیه‌سازی overloading** از default arguments یا `@classmethod` استفاده می‌شود.

```python
class Point:
    def __init__(self, x=0, y=0):  # Default arguments — شبیه‌سازی overloading
        """Create a Point. If no args, defaults to (0, 0)."""
        self.x = x
        self.y = y

# راه‌های مختلف ساختن — شبیه function overloading
p1 = Point()         # (0, 0)
p2 = Point(3)        # (3, 0)
p3 = Point(3, 4)     # (3, 4)
```

---

## Attributeها — Public و "Private"

پایتون access modifier (مثل `private` و `public`) ندارد. به‌جای آن از **قرارداد نام‌گذاری** استفاده می‌شود:

- `name` — public (هر کسی می‌تواند بخواند و تغییر دهد)
- `_name` — "protected" (قرارداد: لطفاً از بیرون استفاده نکن)
- `__name` — name mangling (پایتون نام را به `_ClassName__name` تغییر می‌دهد تا از دسترسی تصادفی جلوگیری کند — نه واقعاً private)

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
print(acc._bank)        # MyBank — کار می‌کند، اما برخلاف قرارداد
# print(acc.__balance)  # AttributeError!
print(acc._BankAccount__balance)  # 1000 — name mangling قابل دور زدن است
```

**فلسفه پایتون:** "We are all consenting adults here." — به برنامه‌نویس اعتماد کن. اگر کسی خواست از `_method` استفاده کند، مسئولیتش با خودش است.

---

## Property — جایگزین Getter/Setter

در C++ برای encapsulation از getter/setter استفاده می‌شود. در پایتون، `@property` این کار را Pythonicتر انجام می‌دهد:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # attribute "private"

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
print(ali.age)       # 25 — به‌جای ali.get_age()
ali.age = 30         # به‌جای ali.set_age(30) — با اعتبارسنجی
print(ali.is_adult)  # True — computed property بدون پرانتز
```

**چرا `@property` پایتونیک است؟**
- خوانایی: `ali.age = 30` طبیعی‌تر از `ali.set_age(30)` است.
- می‌توان بعداً getter/setter اضافه کرد بدون تغییر کد بیرونی.
- computed propertyها بدون پرانتز قابل دسترسی هستند.

---

## متدهای ویژه (Dunder / Magic Methods)

پایتون متدهای ویژه‌ای دارد که با `__` شروع و تمام می‌شوند. این متدها رفتار اشیاء را با عملگرها و توابع built-in تعریف می‌کنند — معادل operator overloading در C++.

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

### جدول متدهای ویژه پرکاربرد

| متد ویژه | عملگر/تابع | معادل C++ |
|---|---|---|
| `__init__` | Constructor | `ClassName(...)` |
| `__del__` | Destructor | `~ClassName()` |
| `__str__` | `print(obj)`, `str(obj)` | `operator<<` یا `ToString()` |
| `__repr__` | `repr(obj)` | خروجی debug |
| `__add__` | `+` | `operator+` |
| `__eq__` | `==` | `operator==` |
| `__len__` | `len(obj)` | `size()` |
| `__getitem__` | `obj[index]` | `operator[]` |
| `__call__` | `obj(args)` | `operator()` |

---

## Class Method و Static Method

پایتون function overloading ندارد، بنابراین نمی‌توان چند constructor با امضاهای مختلف داشت. `@classmethod` این محدودیت را با ایجاد **سازنده‌های جایگزین (Factory Methods)** حل می‌کند.

### سازنده جایگزین — `@classmethod`

پارامتر `cls` (اولین پارامتر) به خود کلاس اشاره می‌کند — مانند `self` که به نمونه اشاره می‌کند. مزیت اصلی: در وراثت، `cls` به کلاس فرزند اشاره می‌کند، نه کلاس والد.

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

# سه راه برای ساختن Person
p1 = Person("Ali", 25)
p2 = Person.from_birth_year("Sara", 1990)
p3 = Person.from_json('{"name":"Reza","age":22}')

# در وراثت، cls به کلاس فرزند اشاره می‌کند
class Employee(Person):
    pass

e = Employee.from_birth_year("Ali", 1990)
print(type(e))  # <class 'Employee'> — نه Person!
```

### تابع کمکی مرتبط با کلاس — `@staticmethod`

یک تابع معمولی که از نظر منطقی به کلاس مربوط است، اما نه به `self` نیاز دارد، نه به `cls`. مانند تابعی که می‌توان بیرون کلاس نوشت، اما برای سازمان‌دهی بهتر داخل کلاس قرار می‌گیرد.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

# بدون ساختن نمونه قابل استفاده است
print(Math.add(3, 5))    # 8
print(Math.is_even(10))  # True
```

### تفاوت انواع متدها

| نوع متد | پارامتر اول | دسترسی به | کاربرد اصلی | معادل C++ |
|---|---|---|---|---|
| Instance | `self` (نمونه) | `self.attr` | کار با داده‌های نمونه | متد معمولی |
| Class | `cls` (کلاس) | `cls.attr`, کلاس | سازنده جایگزین، factory | `static` با template |
| Static | هیچ | هیچ | توابع کمکی مرتبط با کلاس | `static` |

---

## وراثت (Inheritance)

پایتون از وراثت ساده و چندگانه پشتیبانی می‌کند. برخلاف C++، تمام متدها به‌صورت خودکار **virtual** هستند — نیازی به کلمه کلیدی `virtual` نیست.

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

### مقایسه وراثت

| مفهوم | C++ | Python |
|---|---|---|
| وراثت ساده | `class Dog : public Animal { };` | `class Dog(Animal):` |
| وراثت چندگانه | `class C : public A, public B { };` | `class C(A, B):` |
| Virtual method | `virtual void speak();` | همه متدها virtual هستند |
| Pure virtual | `virtual void speak() = 0;` | `raise NotImplementedError` |
| Constructor والد | `Animal(name)` در initializer list | `super().__init__(name)` |
| Destructor virtual | نیاز به `virtual ~Base()` | ندارد — GC مدیریت می‌کند |

---

## Duck Typing — چندریختی بدون وراثت

در C++، برای  polymorphism از طریق inheritance + virtual functions پیاده‌سازی می‌شود. در پایتون، **Duck Typing** جایگزین اصلی است: "اگر شیء متدی به اسم `speak` دارد، می‌توانیم صدایش کنیم — مهم نیست از چه کلاسی آمده."

این روش نیاز به کلاس پایه مشترک را از بین می‌برد و انعطاف‌پذیری را به‌شدت افزایش می‌دهد.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:  # از هیچ کلاسی ارث‌بری نکرده
    def speak(self):
        return "Quack!"

def make_it_speak(thing):
    """Any object with speak() works — no common base class needed."""
    return thing.speak()

print(make_it_speak(Dog()))   # Woof!
print(make_it_speak(Cat()))   # Meow!
print(make_it_speak(Duck()))  # Quack!
```

**کاربرد در Intelligent Systems:** سنسورهای مختلف (`CameraSensor`, `LidarSensor`, `TemperatureSensor`) هر کدام `read()` دارند. با Duck Typing می‌توان همه را یکسان پردازش کرد، بدون اینکه مجبور به ساختن کلاس پایه `SensorBase` باشیم.

```python
def collect_data(sensor):
    return sensor.read()  # هر سنسوری که read() داشته باشد

# همه کار می‌کنند — حتی اگر از کتابخانه‌های مختلف باشند
data = collect_data(camera)       # از کتابخانه A
data = collect_data(lidar)        # از کتابخانه B
data = collect_data(temperature)  # از کتابخانه C
```

---

## اصول چهارگانه شی‌گرایی در پایتون

### ۱. Encapsulation (کپسوله‌سازی)

داده‌ها و متدهای مرتبط در یک کلاس جمع می‌شوند. دسترسی به داده‌های داخلی از طریق قرارداد `_` و `__` و `@property` کنترل می‌شود — نه به‌اجبار کامپایلر، بلکه با اعتماد به برنامه‌نویس.

### ۲. Abstraction (انتزاع)

پیچیدگی‌های داخلی پنهان و فقط یک اینترفیس ساده به بیرون ارائه می‌شود. در پایتون با Duck Typing (هر شیء که متد مورد نظر را داشته باشد) یا با `ABC` + `@abstractmethod` پیاده‌سازی می‌شود.

### ۳. Inheritance (وراثت)

کلاس فرزند ویژگی‌ها و رفتارهای کلاس والد را به ارث می‌برد. در پایتون، Composition (استفاده از شیء به‌عنوان attribute) اغلب بر Inheritance ترجیح داده می‌شود — انعطاف‌پذیری بیشتر و coupling کمتر.

### ۴. Polymorphism (چندریختی)

اشیاء مختلف به یک پیام (متد) یکسان به روش‌های متفاوت پاسخ می‌دهند. در پایتون، Duck Typing روش اصلی polymorphism است — بدون نیاز به inheritance و virtual functions.

---

## Abstract Base Classes — کتابخانه `abc`

اگر می‌خواهی **حتماً** subclasses متد خاصی را implement کنند، از `ABC` و `@abstractmethod` استفاده کن. این شبیه pure virtual functions در C++ است.

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

### مقایسه Abstract Class

| مفهوم | C++ | Python |
|---|---|---|
| تعریف | `class Shape { virtual double area() = 0; };` | `class Shape(ABC): @abstractmethod` |
| Pure virtual | `= 0;` | `@abstractmethod` |
| جلوگیری از instantiation | بله — خطای کامپایل | بله — TypeError در runtime |
| Virtual destructor | نیاز دارد | ندارد |

---

## Dataclass — کلاس‌های داده ساده (Python 3.7+)

`dataclass` خودکار `__init__`, `__repr__`, `__eq__` و متدهای دیگر را تولید می‌کند. معادل `struct` در C++ است.

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
print(p1)           # Point(x=3, y=4) — __repr__ خودکار
print(p1 == p2)     # True — __eq__ خودکار
```

---

## `__slots__` — بهینه‌سازی حافظه

هر نمونه پایتون یک `__dict__` برای ذخیره attributeها دارد که overhead حافظه ایجاد می‌کند. `__slots__` این `__dict__` را حذف می‌کند و فقط attributeهای مشخص‌شده مجاز خواهند بود. مناسب برای وقتی که میلیون‌ها نمونه از یک کلاس می‌سازی.

```python
class Point:
    __slots__ = ("x", "y")  # دیگر نمی‌توان attribute جدید اضافه کرد

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
# p.z = 5  # AttributeError — فقط x و y مجازند
```

---

## Composition over Inheritance

در پایتون، به‌خاطر Duck Typing، معمولاً **Composition** (استفاده از شیء دیگر به‌عنوان attribute) بر **Inheritance** ترجیح داده می‌شود. این کار coupling را کاهش و انعطاف‌پذیری را افزایش می‌دهد.

```python
# Inheritance — سلسله مراتب صلب
class Robot:
    def move(self):
        pass

class FlyingRobot(Robot):
    def fly(self):
        pass

# Composition — انعطاف‌پذیرتر
class FlyBehavior:
    def fly(self):
        return "Flying"

class Robot:
    def __init__(self, behavior):
        self.behavior = behavior  # رفتار به‌عنوان attribute

    def perform_action(self):
        return self.behavior.fly()  # هر رفتاری که fly() داشته باشد

robot = Robot(FlyBehavior())
print(robot.perform_action())  # Flying
```

---

## نکات کلیدی این فصل

1. **کلاس‌ها با `class` تعریف می‌شوند و `self` معادل صریح `this` در C++ است.** نوشتن `self` به‌عنوان اولین پارامتر تمام متدهای نمونه اجباری است.

2. **پایتون access modifier اجباری ندارد.** از قرارداد `_` (protected) و `__` (name mangling) استفاده می‌شود. فلسفه: "We are all consenting adults."

3. **در پایتون `@property` جایگزین پایتونیک getter/setter است.** خوانایی بالاتر، قابلیت افزودن اعتبارسنجی بدون تغییر کد بیرونی، و computed property بدون پرانتز.

4. **پایتون function overloading ندارد.** با default arguments و `@classmethod` (سازنده‌های جایگزین) این محدودیت جبران می‌شود.

5. **در پایتون `@classmethod` برای factory methods استفاده می‌شود.** `cls` به کلاس (یا subclass در وراثت) اشاره می‌کند. `@staticmethod` برای توابع کمکی است که نه `self` نیاز دارند، نه `cls`.

6. **همه متدها virtual هستند.** polymorphism خودکار است — بدون نیاز به `virtual` و `override`.

7. **در پایتون Duck Typing روش اصلی polymorphism است.** "اگر مثل اردک راه می‌رود، اردک است." هر شیئی که متد مورد نظر را داشته باشد قابل استفاده است — بدون نیاز به کلاس پایه مشترک.

8. **در پایتون Abstract Base Classes (`abc`) برای اجبار به implement متدها استفاده می‌شوند.** معادل pure virtual functions در C++.

9. **در پایتون `dataclass` معادل `struct` در C++ است.** خودکار `__init__`, `__repr__`, `__eq__` تولید می‌کند.

10. **در پایتون `__slots__` مصرف حافظه را برای کلاس‌هایی با نمونه‌های زیاد بهینه می‌کند.** اما انعطاف‌پذیری افزودن attribute جدید را از بین می‌برد.

11. **در پایتون Composition بر Inheritance ترجیح داده می‌شود.** انعطاف‌پذیری بیشتر، coupling کمتر.

12. **متدهای ویژه (Dunder Methods) معادل operator overloading در C++ هستند.** `__add__` برای `+`، `__eq__` برای `==`، `__call__` برای `operator()` و غیره.

13. **توابع در پایتون خودشان object هستند.** آرگومان‌های پیش‌فرض mutable فقط یک بار (هنگام `def`) ساخته می‌شوند (از فصل ۸).

---

## پرسش و پاسخ (Q&A)

### سوال: `@classmethod` و `@staticmethod` چه کاربردی دارند و چه فرقی با هم دارند؟
**پاسخ:** `@classmethod` برای ساختن constructorهای جایگزین (factory methods) استفاده می‌شود — `cls` به کلاس اشاره می‌کند و در وراثت، نوع واقعی subclass را منعکس می‌کند. `@staticmethod` یک تابع معمولی داخل کلاس است که فقط برای سازمان‌دهی بهتر آنجا قرار گرفته — نه `self` دارد، نه `cls`. در C++، `@staticmethod` معادل مستقیم `static` است، اما `@classmethod` معادل مستقیمی ندارد.

### سوال: Duck Typing دقیقاً چه مشکلی را حل می‌کند؟
**پاسخ:** نیاز به کلاس پایه مشترک را از بین می‌برد. در C++، برای پردازش یکسان اشیاء مختلف، یا باید از inheritance استفاده کنی (که coupling ایجاد می‌کند) یا از templates (که در زمان کامپایل بررسی می‌شوند). Duck Typing در پایتون اجازه می‌دهد هر شیئی که متد مورد نظر را داشته باشد قابل استفاده باشد — حتی اگر از کتابخانه‌های کاملاً متفاوت آمده باشد.

### سوال: اصول چهارگانه شی‌گرایی در پایتون چطور پیاده‌سازی می‌شوند؟
**پاسخ:** Encapsulation با قرارداد `_` و `@property` (نه با اجبار کامپایلر). Abstraction با Duck Typing یا `ABC`. Inheritance با `class D(B):` اما Composition اغلب بهتر است. Polymorphism عمدتاً با Duck Typing — بدون نیاز به inheritance و virtual functions.

### سوال: Abstract Base Class چه زمانی باید استفاده شود؟
**پاسخ:** وقتی می‌خواهی **اجبار کنی** که subclasses حتماً متد خاصی را implement کنند. مانند pure virtual functions در C++. اگر به این اجبار نیاز نداری، Duck Typing کافی و پایتونیک‌تر است.

### سوال: چرا پایتون `private` واقعی ندارد؟
**پاسخ:** فلسفه پایتون "We are all consenting adults" است — به برنامه‌نویس اعتماد می‌کند. `__` (name mangling) برای جلوگیری از تصادم نام‌ها در وراثت طراحی شده، نه برای امنیت. این فلسفه انعطاف‌پذیری را به قیمت از دست دادن برخی تضمین‌های زمان کامپایل می‌پذیرد.

---

# بخش الحاقی به README_fa.md فصل ۰۹

## Composition vs Inheritance — معماری ماژولار

### مشکل Inheritance

وراثت رابطه **is-a** (یک ... هست) می‌سازد. این رابطه صلب است و با افزایش قابلیت‌ها، تعداد کلاس‌ها از کنترل خارج می‌شود:

```python
class Robot:
    def move(self):
        print("Moving...")

class FlyingRobot(Robot):
    def fly(self):
        print("Flying...")

class SwimmingRobot(Robot):
    def swim(self):
        print("Swimming...")

# اگر رباتی بخواهیم که هم پرواز کند هم شنا:
# class FlyingSwimmingRobot(Robot): ... — کلاس جدید لازم است
# این یعنی انفجار ترکیبی (Combinatorial Explosion)
```

### راه‌حل: Composition

[فارسی] Composition رابطه **has-a** (یک ... دارد) می‌سازد. رفتارها به‌عنوان اجزای قابل تعویض به کلاس تزریق می‌شوند:

```python
#[Farsi]
# رفتارها به‌عنوان کلاس‌های مستقل — هر کدام یک قابلیت
class WalkBehavior:
    def move(self):
        return "Walking forward..."

class FlyBehavior:
    def move(self):
        return "Flying high!"

class SwimBehavior:
    def move(self):
        return "Swimming deep!"

# ربات یک پلتفرم است — رفتار از بیرون تزریق می‌شود
class Robot:
    def __init__(self, name, movement):
        self.name = name
        self.movement = movement  # Composition: Robot HAS-A movement

    def move(self):
        return f"{self.name}: {self.movement.move()}"

# مونتاژ ربات‌ها با ترکیب‌های دلخواه — بدون نوشتن کلاس جدید
ground_robot = Robot("R1", WalkBehavior())
flying_robot = Robot("R2", FlyBehavior())
swimming_robot = Robot("R3", SwimBehavior())

print(ground_robot.move())   # R1: Walking forward...
print(flying_robot.move())   # R2: Flying high!
print(swimming_robot.move()) # R3: Swimming deep!

# ارتقا در زمان اجرا — تغییر رفتار بدون تغییر کلاس Robot
ground_robot.movement = FlyBehavior()  # حالا پرواز می‌کند
```

### مزایای Composition

- **انعطاف‌پذیری:** رفتارها مانند قطعات لگو ترکیب می‌شوند — بدون تغییر کد کلاس اصلی.
- **[فارسی] Coupling کمتر:** کلاس Robot به پیاده‌سازی خاصی وابسته نیست — فقط کافی است رفتار یک متد `move()` داشته باشد.
- **تست‌پذیری:** هر رفتار را می‌توان جداگانه تست کرد.
- **ارتقا در زمان اجرا:** رفتار یک نمونه را می‌توان در حین اجرا تغییر داد.

### ارتباط با Plugin-Based Architecture و Strategy Pattern

[فارسی] Plugin-Based Architecture و Strategy Pattern هر دو از Composition استفاده می‌کنند:

- **[فارسی] Strategy Pattern:** رفتار (Strategy) به‌عنوان یک شیء مجزا تعریف و به Context تزریق می‌شود. Context فقط اینترفیس را می‌شناسد، نه پیاده‌سازی.
- **[فارسی] Plugin Architecture:** سیستم یک هسته (Core) دارد که فقط اینترفیس‌ها را تعریف می‌کند. قابلیت‌ها به‌عنوان پلاگین اضافه می‌شوند — بدون تغییر کد هسته.

```python
# Plugin Architecture با استفاده از Composition

class RobotCore:
    """هسته ربات — فقط اینترفیس‌ها را می‌شناسد."""
    
    def __init__(self):
        self.movement_plugin = None
        self.sensor_plugin = None
    
    def load_movement(self, plugin):
        """هر پلاگینی که move() داشته باشد."""
        self.movement_plugin = plugin
    
    def load_sensor(self, plugin):
        """هر پلاگینی که read() داشته باشد."""
        self.sensor_plugin = plugin
    
    def operate(self):
        data = self.sensor_plugin.read()
        self.movement_plugin.move()

# پلاگین‌ها — هر کسی می‌تواند بنویسد، بدون تغییر RobotCore
class Wheels:
    def move(self):
        return "Moving on wheels"

class Propellers:
    def move(self):
        return "Flying with propellers"

class Camera:
    def read(self):
        return "Camera image"

class Lidar:
    def read(self):
        return "Lidar point cloud"

# مونتاژ و ارتقا بدون تغییر RobotCore
robot = RobotCore()
robot.load_movement(Wheels())
robot.load_sensor(Camera())
robot.operate()

# ارتقا به ربات پرنده با سنسور بهتر
robot.load_movement(Propellers())
robot.load_sensor(Lidar())
robot.operate()
```

### قانون طلایی

- **[فارسی] Inheritance** برای رابطه **is-a** (چیستی): `class IndustrialRobot(Robot):` — IndustrialRobot **یک نوع** Robot است.
- **[فارسی] Composition** برای رابطه **has-a** (قابلیت‌ها): `self.movement = Wheels()` — Robot **یک** قابلیت حرکت **دارد**.

در دنیای واقعی، معمولاً ترکیبی از هر دو استفاده می‌شود: Inheritance برای تعریف هویت (identity) و Composition برای تعریف قابلیت‌ها (capabilities).