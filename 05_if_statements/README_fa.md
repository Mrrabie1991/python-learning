# ۰۵ - دستورات شرطی (if Statements)

## ساختار پایه if/elif/else

پایتون به‌جای `{}` از تورفتگی (indentation) برای تعیین محدوده بلوک‌ها استفاده می‌کند.

```python
x = 10

if x > 5:
    print("x is greater than 5")

if x > 20:
    print("x is greater than 20")
else:
    print("x is not greater than 20")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### مقایسه با C++

| C++ | Python |
|---|---|
| `if (condition) { }` | `if condition:` |
| `else if` | `elif` |
| `else { }` | `else:` |
| `{}` برای بلوک | `:` + تورفتگی (۴ فاصله) |
| `switch (x) { }` | `match x:` (Python 3.10+) |

## تورفتگی (Indentation)

در C++، تورفتگی برای خوانایی است و اختیاری. در پایتون، بخشی از نحو زبان و اجباری است.
قرارداد رسمی (PEP 8): ۴ فاصله (space) برای هر سطح. Tab استفاده نشود.

```python
#true صحیح
if x > 5:
    print("Hello")
    print("World")

# خطا — تورفتگی نامنظم
if x > 5:
    print("Hello")
  print("World")  # IndentationError
```

## عملگرهای مقایسه و منطقی

### مقایسه (مانند C++)

```python
5 == 5    # True
5 != 3    # True
5 > 3     # True
5 < 3     # False
5 >= 5    # True
5 <= 3    # False
```

### منطقی (کلمات کلیدی به‌جای && و ||)

```python
a, b = True, False
a and b   # False — معادل &&
a or b    # True  — معادل ||
not a     # False — معادل !
```

### مقایسه زنجیره‌ای (Chained Comparisons)

در C++ باید بنویسید `x > 2 && x < 10`. در پایتون:

```python
x = 5
2 < x < 10    # True
10 < x < 20   # False
```

| عملگر | C++ | Python |
|---|---|---|
| AND | `&&` | `and` |
| OR | `\|\|` | `or` |
| NOT | `!` | `not` |
| بازه | `x > 2 && x < 10` | `2 < x < 10` |

## مقدارهای Truthy و Falsy

در C++، فقط `0` و `false` و `nullptr` در شرط false هستند. در پایتون، هر چیزی یک مقدار بولی دارد.

### مقادیر Falsy (تبدیل به False می‌شوند)

```python
bool(0)        # False
bool(0.0)      # False
bool("")       # False — رشته خالی
bool([])       # False — لیست خالی
bool(())       # False — tuple خالی
bool({})       # False — دیکشنری خالی
bool(set())    # False — مجموعه خالی
bool(None)     # False
```

### مقادیر Truthy (همه چیز دیگر)

```python
bool(1)        # True
bool(-1)       # True
bool("Hello")  # True
bool([1, 2])   # True
bool({"a": 1}) # True
```

### کاربرد عملی

```python
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")

items = []
if not items:
    print("List is empty")
```

## عبارت شرطی یک‌خطی — Ternary Operator 

```python
x = 10
result = 100 if x > 5 else 200  # C++: (x > 5) ? 100 : 200
status = "pass" if x >= 10 else "fail"
```

| C++ | Python |
|---|---|
| `condition ? true_val : false_val` | `true_val if condition else false_val` |

## match-case — معادل switch (Python 3.10+)

```python
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:  # default
        print("Unknown command")
```

### Pattern Matching پیشرفته

`match-case` فراتر از `switch` در C++ است و می‌تواند ساختار اشیاء را تجزیه کند (destructuring):

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On y-axis at y={y}")
    case (x, 0):
        print(f"On x-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

نحوه اجرا:

۱.الف `point = (0, 5)` — یک tuple با دو عنصر.

۲.ب `case (0, 0):` — عنصر اول و دوم هر دو ۰؟ خیر، رد می‌شود.

۳.ج `case (0, y):` — عنصر اول ۰ است؟ بله. عنصر دوم در متغیر `y` قرار می‌گیرد (`y = 5`). چاپ می‌کند: `On y-axis at y=5`.

۴.د اجرای `match` متوقف می‌شود — فقط اولین الگوی منطبق اجرا می‌شود.

۵.ه `case (x, y):` یک catch-all است (مانند `default`) و هر چیزی را match می‌کند.


##  داخل شرط Assignment ممنوع است

در C++:
```cpp
if (x = 5) {  // کامپایل می‌شود ولی باگ است — ۵ همیشه true
}
```

در پایتون:
```python
if x = 5:  # SyntaxError — پایتون اجازه نمی‌دهد
```

پایتون عمداً این کار را ممنوع کرده تا از این باگ کلاسیک جلوگیری کند.

## x++ و ++x در پایتون وجود ندارند

در پایتون `x++` و `++x`  تعریف نشده‌اند و خطای نحوی می‌دهند. دلیل: `int` در پایتون immutable است و پایتون عملگرهای in-place ضمنی را پشتیبانی نمی‌کند.

```python
x = 0
x += 1  # معادل x = x + 1 — شیء جدید می‌سازد و rebind می‌کند
x -= 1
```

توجه: `+=` روی `int` (immutable) شیء جدید می‌سازد، ولی روی `list` (mutable) خود شیء را تغییر می‌دهد.

## بررسی None با is

همیشه `None` را با `is` بررسی کنید، نه `==`:

```python
x = None
if x is None:      # درست و Pythonic
    print("x is None")
if x == None:      # کار می‌کند ولی Pythonic نیست
    print("x is None")
```

دلیل: `None` یک singleton است (فقط یک نسخه از آن وجود دارد). `is` هویت را بررسی می‌کند و سریع‌تر و صریح‌تر است.

---

## پرسش و پاسخ (Q&A)

### سوال: `set` چیست ؟
**پاسخ:** `set` یک مجموعه از عناصر یکتا و نامرتب است (مانند `std::unordered_set` در C++). خالی بودن آن falsy است.  `set` در فصل ۶ تدریس خواهد شد.

### سوال: `match-case` با pattern matching دقیقاً چه می‌کند؟
**پاسخ:** `match` مقدار را به ترتیب با الگوهای (pattern) هر `case` مقایسه می‌کند. اولین الگوی منطبق اجرا می‌شود و بقیه نادیده گرفته می‌شوند. الگوها می‌توانند متغیرهایی برای استخراج (destructure) مقادیر داشته باشند. این قابلیت فراتر از `switch` در C++ است.

### سوال: چرا `x++` و `++x` در پایتون وجود ندارند؟
**پاسخ:** چون `int` در پایتون immutable است و نمی‌توان آن را درجا (in-place) تغییر داد. پایتون افزایش را با `x += 1` انجام می‌دهد که معادل `x = x + 1` است و یک شیء جدید می‌سازد.