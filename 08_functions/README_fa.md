# ۰۸ - توابع (Functions)

## تعریف تابع — مقایسه با C++

در پایتون، توابع با کلمه کلیدی `def` تعریف می‌شوند. برخلاف C++، نوع پارامترها و نوع بازگشتی اجباری نیست (اما به‌صورت اختیاری با Type Hints قابل تعریف است). هر تابعی که `return` صریح نداشته باشد، `None` برمی‌گرداند. `None` یک شیء از نوع `NoneType` است — برخلاف `void` در C++ که "هیچ" است، `None` یک مقدار واقعی محسوب می‌شود.

**کاربرد در Intelligent Systems:** توابع، واحدهای اصلی سازمان‌دهی منطق برنامه هستند — از پردازش داده حسگرها تا اجرای الگوریتم‌های تصمیم‌گیری. در سیستم‌های هوشمند، توابع کوتاه و تک‌مسئولیتی (Single Responsibility) به تست‌پذیری و نگهداری بهتر کمک می‌کنند.

### تعریف و فراخوانی

```python
# C++:
# int add(int a, int b) {
#     return a + b;
# }

def add(a, b):
    """Return the sum of a and b."""  # docstring — قابل دسترسی در زمان اجرا
    return a + b

print(add(3, 5))  # 8

# تابع بدون return — None برمی‌گرداند
def greet(name):
    """Print a greeting. Returns None implicitly."""
    print(f"Hello, {name}!")

result = greet("Ali")  # "Hello, Ali!"
print(result)          # None
```

### مستندسازی قابل اجرا — docstring

` مستندسازی قابل اجرا — docstring` (مخفف documentation string) یک رشته چندخطی است که اولین عبارت داخل تابع، کلاس، یا ماژول قرار می‌گیرد. برخلاف کامنت در C++،در پایتون  `docstring` در زمان اجرا از طریق `help()` و `.__doc__` در دسترس است.

```python
def add(a, b):
    """Return the sum of a and b.

    This is a docstring — accessible via help(add) or add.__doc__
    """
    return a + b

print(add.__doc__)
help(add)  # docstring را نمایش می‌دهد
```

### مقایسه کلی

| C++ | Python |
|---|---|
| `int add(int a, int b) { return a + b; }` | `def add(a, b): return a + b` |
| `void greet(string name) { }` | `def greet(name): ...` (None برمی‌گرداند) |
| `/** ... */` — کامنت، در زمان اجرا در دسترس نیست | `"""docstring"""` — در `__doc__` ذخیره می‌شود |
| Return type اجباری | ندارد (Dynamic Typing) |
| Parameter type اجباری | ندارد (Type Hints اختیاری) |

---

## پارامترها و آرگومان‌ها — عبور به تابع

در پایتون، همه چیز با **reference** پاس داده می‌شود (مثل `&` در C++). اما رفتار آن بستگی به mutable یا immutable بودن شیء دارد. این دقیقاً همان مدل Name Binding است که در فصل ۰۲ یاد گرفتی.

```python
#[Farsi]
# پارامتر immutable — رفتار شبیه const & در C++
def increment(x):
    """Rebinds x to a new object — original is untouched."""
    x = x + 1
    return x

num = 5
result = increment(num)
print(f"num: {num}, result: {result}")  # num: 5, result: 6

# پارامتر mutable — رفتار شبیه & در C++
def append_item(lst, item):
    """Modifies the original object — NOT rebinding."""
    lst.append(item)

numbers = [1, 2, 3]
append_item(numbers, 4)
print(numbers)  # [1, 2, 3, 4] — original changed!
```

**نکته کلیدی:** پاس دادن immutable (مثل int, str, tuple) به تابع مانند `const &` در C++ عمل می‌کند — تابع نمی‌تواند شیء اصلی را تغییر دهد. پاس دادن mutable (مثل list, dict, set) مانند `&` در C++ عمل می‌کند — تابع می‌تواند محتوای شیء اصلی را تغییر دهد.

---

##   عمر متغیرها و Scope

در پایتون، **فقط توابع** scope جدید می‌سازند. حلقه‌ها، شرط‌ها، و بلوک‌های `with` scope جدید ایجاد نمی‌کنند. این یک تفاوت بنیادی با C++ است.

```python
#[Farsi]
# متغیر تعریف‌شده در حلقه، بیرون حلقه هم در دسترس است
for i in range(3):
    x = i * 2
print(x)  # 4 — در C++ این خطا بود

while True:
    message = input("Enter: ")
    if message == "quit":
        break
print(message)  # "quit" — متغیر بیرون حلقه هم زنده است
```

عمر متغیرها در پایتون توسط **Garbage Collector** تعیین می‌شود، نه صرفاً با پایان scope. یک شیء فقط زمانی از حافظه پاک می‌شود که **هیچ رفرنسی** به آن وجود نداشته باشد. اگر تابعی یک شیء را `return` کند، آن شیء همچنان زنده می‌ماند — حتی اگر scope تابع تمام شده باشد.

```python
def create_list():
    x = [1, 2, 3]  # x در این scope تعریف می‌شود
    return x        # اما شیء بازگردانده می‌شود

result = create_list()  # result به لیست اشاره می‌کند
print(result)           # [1, 2, 3] — لیست هنوز زنده است
```

---

## آرگومان‌های پیش‌فرض  — Default Arguments

پایتون مانند C++ از آرگومان‌های پیش‌فرض پشتیبانی می‌کند. اما یک تفاوت حیاتی وجود دارد: **آرگومان‌های پیش‌فرض mutable فقط یک بار (هنگام تعریف تابع) ساخته می‌شوند**، نه هر بار که تابع فراخوانی می‌شود. این یک باگ کلاسیک پایتون است.

```python
# DANGER — mutable default: only created ONCE at function definition
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] — WTF?! Shared list!
print(add_item(3))  # [1, 2, 3]

# راه درست
def add_item_correct(item, lst=None):
    if lst is None:
        lst = []  # هر بار لیست جدید می‌سازد
    lst.append(item)
    return lst

print(add_item_correct(1))  # [1]
print(add_item_correct(2))  # [2]
```

**چرا این اتفاق می‌افتد؟** توابع در پایتون خودشان object هستند. آرگومان‌های پیش‌فرض در attributeای به نام `__defaults__` ذخیره می‌شوند و فقط یک بار (هنگام `def`) مقداردهی می‌شوند. همه فراخوانی‌های تابع همان یک شیء را به اشتراک می‌گذارند. راه‌حل استاندارد: از `None` به‌عنوان پیش‌فرض استفاده کن و داخل تابع چک کن.

---

## عبور با نام — Keyword Arguments

پایتون اجازه می‌دهد آرگومان‌ها را با نام (و نه بر اساس موقعیت) به تابع پاس دهی. این قابلیتی است که در C++ وجود ندارد (مگر با designated initializers در C++20، آن هم فقط برای structها).

```python
def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old, lives in {city}")

# Positional (مثل C++)
describe_person("Ali", 25, "Tehran")

# Keyword — ترتیب مهم نیست
describe_person(age=30, name="Sara", city="Isfahan")

# ترکیبی — positional اول، سپس keyword
describe_person("Reza", city="Shiraz", age=22)
```

**نکته پایتونیک:** keyword arguments خوانایی کد را به‌شدت بالا می‌برند، مخصوصاً برای توابعی با پارامترهای زیاد یا پارامترهای boolean که معنی موقعیتیشان مبهم است.

---

## تعداد متغیر آرگومان — `*args` و `**kwargs`

پایتون به‌جای `...` (variadic arguments) در C++ از `*args` (برای آرگومان‌های positional) و `**kwargs` (برای آرگومان‌های keyword) استفاده می‌کند. این مکانیزم امن‌تر و انعطاف‌پذیرتر از C++ است.

- `*args` — آرگومان‌های positional اضافی را در یک **tuple** جمع‌آوری می‌کند.
- `**kwargs` — آرگومان‌های keyword اضافی را در یک **dict** جمع‌آوری می‌کند.
- نام‌های `args` و `kwargs` قراردادی هستند — آنچه اهمیت دارد `*` و `**` است.

```python
# *args — variable positional arguments
def sum_all(*args):
    """Return the sum of all arguments. args is a tuple."""
    return sum(args)

print(sum_all(1, 2, 3))       # 6
print(sum_all(1, 2, 3, 4, 5)) # 15

# **kwargs — variable keyword arguments
def print_info(**kwargs):
    """Print all key-value pairs. kwargs is a dict."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ali", age=25, city="Tehran")

# ترکیب هر دو
def full_signature(required, *args, default="x", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"default: {default}")
    print(f"kwargs: {kwargs}")

full_signature("req", "a", "b", "c", default="y", name="Ali", age=25)
```

---

## توابع بی‌نام — Lambda Functions

 در پایتون `lambda` یک تابع بی‌نام است که **فقط یک expression** می‌تواند داشته باشد (نه statement). برخلاف C++ که lambda می‌تواند چندین statement داشته باشد، lambda در پایتون بسیار محدودتر است. برای منطق پیچیده‌تر، از `def` استفاده کن.

```python
# C++ lambda:
# auto add = [](int a, int b) { return a + b; };

# Python lambda — فقط یک expression
add = lambda a, b: a + b
print(add(3, 5))  # 8

# کاربرد رایج — کلید مرتب‌سازی
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Reza", "score": 78},
]
sorted_by_score = sorted(students, key=lambda s: s["score"])

# Lambda در map/filter
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

| ویژگی | C++ Lambda | Python Lambda |
|---|---|---|
| بدنه | چندین statement | فقط یک expression |
| Capture | دستی با `[=, &x]` | خودکار — هر چه در scope باشد |
| نگهداری | `auto` یا `std::function` | متغیر معمولی |

**نکته پایتونیک:** در بسیاری از موارد، list comprehension یا generator expression جایگزین خواناتری برای `map`/`filter` با lambda است.

```python
#[Farsi]
# روش پایتونیک‌تر
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

---

## نشانه‌گذاری نوع (اختیاری) — Type Hints

در پایتون Type Hints **کاملاً اختیاری** هستند و در زمان اجرا بررسی نمی‌شوند (مگر با ابزارهای static analysis مثل mypy). برای توابع، استفاده از آنها پایتونیک و توصیه‌شده است. برای متغیرهای محلی، کمتر رایج است.

```python
from typing import List, Dict, Optional

# Type hints برای تابع — پایتونیک و توصیه‌شده
def calculate_average(scores: list[int]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

# Type hints برای متغیر — اختیاری، کمتر رایج
x: int = 10
name: str = "Ali"
data: dict[str, int] = {"a": 1, "b": 2}

# پایتون نوع‌ها را در زمان اجرا بررسی نمی‌کند
x = "Hello"  # کاملاً قانونی — هیچ خطایی رخ نمی‌دهد
```

**توصیه:** برای امضای توابع (پارامترها و بازگشتی) از Type Hints استفاده کن — خوانایی و نگهداری کد را بهبود می‌بخشد. برای متغیرهای داخلی تابع، ضرورتی ندارد.

---

## حافظه و بهینه‌سازی — نکات تکمیلی برای مهندسان C++

### Integer Caching

اعداد صحیح کوچک (معمولاً ۵- تا ۲۵۶) در CPython از پیش ساخته و کش می‌شوند. این یعنی:

```python
x = 1
y = 1
print(x is y)  # True — هر دو به همون شیء کش‌شده اشاره می‌کنند

a = 1000
b = 1000
print(a is b)  # False — اعداد بزرگ هر بار شیء جدید می‌سازند
```

### هزینه relative — mutate vs rebind

```python
# rebind — لیست جدید + (احتمالاً) اشیاء جدید
x = [1, 2]
x = [3, 4]  # لیست قدیمی GC می‌شود، لیست جدید ساخته می‌شود

# mutate — خود لیست می‌ماند، فقط اشاره‌گرهای داخلی تغییر می‌کنند
x = [1, 2]
x[0] = 5    # لیست همان است، اشاره‌گر اول rebind می‌شود
```

(تغییر درجا) mutate کردن  کم‌هزینه‌تر از rebind کردن (ساختن لیست جدید) است. اما در عمل، GC پایتون برای اکثر کاربردها به‌اندازه کافی سریع هست.

### لیست برای شبیه‌سازی "متغیر mutable" بهینه نیست

```python
#[Farsi]
# روش ۱: int مستقیم — ۱ شیء
x = 5

# روش ۲: int در لیست — ۲ شیء (لیست + int)
x = [5]
```

استفاده از لیست برای شبیه‌سازی متغیر mutable نه تنها حافظه را بهینه نمی‌کند، بلکه مصرف را افزایش می‌دهد. خود لیست یک شیء اضافی با سربار اشاره‌گرهاست.

---

## نکات کلیدی این فصل

1. **توابع با `def` تعریف می‌شوند و در صورت نبود `return`، `None` برمی‌گردانند.** `None` یک شیء است، نه "هیچ".

2. **همه چیز با reference پاس داده می‌شود.** رفتار برای immutableها شبیه `const &` و برای mutableها شبیه `&` در C++ است.

3. **فقط توابع scope جدید می‌سازند.** حلقه‌ها، شرط‌ها، و `with` scope جدید ایجاد نمی‌کنند.

4. **عمر متغیرها توسط GC تعیین می‌شود، نه scope.** شیء تا زمانی که رفرنسی به آن باشد زنده می‌ماند.

5. **هرگز از mutable به‌عنوان آرگومان پیش‌فرض استفاده نکن.** از `None` استفاده کن و داخل تابع چک کن.

6. **[فارسی] keyword arguments خوانایی را بالا می‌برند و پایتونیک هستند.**

7. **[فارسی] `*args` و `**kwargs` جایگزین امن و انعطاف‌پذیر `...` در C++ هستند.**

8. **[فارسی] lambda در پایتون فقط یک expression می‌تواند داشته باشد.** برای منطق پیچیده از `def` استفاده کن.

9. **[فارسی] Type Hints برای توابع توصیه می‌شوند، برای متغیرهای محلی اختیاری هستند.** در زمان اجرا بررسی نمی‌شوند.

10. **توابع در پایتون خودشان object هستند.** آرگومان‌های پیش‌فرض در `__defaults__` ذخیره می‌شوند و فقط یک بار مقداردهی می‌شوند.

11. **[فارسی] mutate کردن از rebind کردن کم‌هزینه‌تر است، ولی GC پایتون برای اکثر کاربردها سریع است.**

12. **اعداد کوچک (-5 تا 256) در CPython کش می‌شوند و GC نمی‌شوند.**

---

## پرسش و پاسخ (Q&A)

### سوال: عمر متغیرها در پایتون چگونه است؟ آیا مثل C++ با پایان scope تمام می‌شود؟
**پاسخ:** خیر. فقط توابع scope جدید می‌سازند. حلقه‌ها و شرط‌ها scope جدید نمی‌سازند. همچنین، عمر شیء توسط Garbage Collector تعیین می‌شود — تا زمانی که رفرنسی به شیء وجود داشته باشد، زنده می‌ماند، حتی اگر scope تابع تمام شده باشد (مثلاً با `return`).

### سوال: چرا متغیر تعریف‌شده در حلقه، بیرون حلقه هم قابل دسترسی است؟
**پاسخ:** چون پایتون برای حلقه‌ها scope جدید نمی‌سازد. فقط `def`، `class`، و `lambda` scope جدید ایجاد می‌کنند. این یک تفاوت بنیادی با C++ است.

### سوال: چرا `lst=[]` در آرگومان پیش‌فرض باعث اشتراک لیست بین فراخوانی‌ها می‌شود؟
**پاسخ:** توابع در پایتون object هستند. آرگومان‌های پیش‌فرض یک بار (هنگام `def`) ساخته و در `__defaults__` تابع ذخیره می‌شوند. هر فراخوانی که آرگومان را پاس ندهد، از همان شیء ذخیره‌شده استفاده می‌کند. راه‌حل: از `None` به‌عنوان پیش‌فرض استفاده کن و داخل تابع لیست جدید بساز.

### سوال: آیا `z[0] = 5` باعث rebinding خود `z` می‌شود یا فقط اشاره‌گر داخلی تغییر می‌کند؟
**پاسخ:** فقط اشاره‌گر داخلی تغییر می‌کند. `z` همچنان به همان شیء لیست اشاره می‌کند (`id(z)` ثابت است). اشاره‌گر `z[0]` از شیء قبلی جدا شده و به شیء جدید (`int(5)`) اشاره می‌کند. این مانند تغییر یک pointer در آرایه‌ای از pointerهاست.

### سوال: آیا استفاده از لیست تک‌عنصری به‌جای متغیر immutable مصرف حافظه را بهینه می‌کند؟
**پاسخ:** خیر. لیست خودش یک شیء اضافی با سربار اشاره‌گرهاست. `x = [5]` دو شیء می‌سازد (لیست + int)، در حالی که `x = 5` فقط یک شیء. استفاده از لیست برای شبیه‌سازی "متغیر mutable" مصرف حافظه را افزایش می‌دهد، نه کاهش.

### سوال: آیا `x = [1,2]` و سپس `x = [3,4]` سه زباله تولید می‌کند؟
**پاسخ:** لیست قبلی حتماً GC می‌شود. اما اعداد 1 و 2 اگر بین -5 تا 256 باشند، در CPython کش می‌شوند و GC نمی‌شوند. اگر اعداد بزرگ باشند، آنها هم GC می‌شوند. در مجموع: ۱ تا ۳ شیء بسته به اندازه اعداد.

### سوال: آیا C++ از keyword arguments پشتیبانی می‌کند؟
**پاسخ:** خیر، C++ keyword argument واقعی به سبک پایتون ندارد. اگر همه پارامترها default داشته باشند، می‌توان بعضی را skip کرد، اما همچنان ترتیب positional باید رعایت شود. نوشتن `f(b=20)` در C++ خطاست.

### سوال: docstring چه تفاوتی با کامنت دارد؟
**پاسخ:** docstring (بین `""" """`) در `__doc__` شیء ذخیره می‌شود و در زمان اجرا از طریق `help()` قابل دسترسی است. کامنت (`#` یا `/** */`) فقط برای خوانایی است و در زمان اجرا وجود ندارد. docstring استاندارد مستندسازی در پایتون است.