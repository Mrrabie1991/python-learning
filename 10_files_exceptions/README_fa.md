# ۱۰ - فایل‌ها و استثناها (Files & Exceptions)

## خواندن و نوشتن فایل

کار با فایل در پایتون از طریق تابع built-in به اسم `open()` و context manager با `with` انجام می‌شود. `with` تضمین می‌کند که فایل حتماً بسته شود — حتی اگر در حین کار خطایی رخ دهد. این معادل RAII در C++ است.

**کاربرد در Intelligent Systems:** خواندن داده‌های حسگرها از فایل‌های CSV، ذخیره‌سازی پیکربندی سیستم در JSON، ثبت لاگ رویدادها، و پردازش دیتاست‌های بزرگ.

```python
#[Farsi]
# نوشتن در فایل — C++: ofstream file("output.txt"); file << "Hello";
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("This is line 2.\n")

# خواندن کل فایل — C++: string s((istreambuf_iterator<char>(f)), ...);
with open("output.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# خواندن خط به خط — C++: getline(file, line)
with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# خواندن همه خطوط به صورت لیست
with open("output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

### مقایسه با C++

| عملیات | C++ | Python |
|---|---|---|
| نوشتن فایل | `std::ofstream f("out.txt"); f << "text"; f.close();` | `with open("out.txt", "w") as f: f.write("text")` |
| خواندن کل فایل | `std::ifstream f("in.txt"); std::string s(...);` | `content = f.read()` |
| خواندن خط به خط | `std::getline(f, line)` | `for line in file:` |
| بستن فایل | `f.close()` (دستی یا RAII) | خودکار با `with` |

### مودهای باز کردن فایل

| Mode | توضیح | معادل C++ |
|---|---|---|
| `"r"` | خواندن (فایل باید وجود داشته باشد) | `ios::in` |
| `"w"` | نوشتن (فایل ساخته یا بازنویسی می‌شود) | `ios::out` |
| `"a"` | افزودن به انتها (append) | `ios::app` |
| `"x"` | ایجاد فایل جدید — اگر وجود داشته باشد خطا | — |
| `"rb"` | خواندن باینری | `ios::in \| ios::binary` |
| `"wb"` | نوشتن باینری | `ios::out \| ios::binary` |

---

## دستور `with` — معادل RAII در C++

دستور `with` در پایتون یک context manager است که تضمین می‌کند منبع (فایل، شبکه، قفل) **حتماً** آزاد شود، حتی اگر استثنایی رخ دهد. این دقیقاً فلسفه RAII در C++ است.

```cpp
// C++ RAII — destructor file را می‌بندد
{
    std::ifstream file("data.txt");
    // ... read ...
}  // file automatically closed — even if exception thrown
```

```python
# Python with — context manager
with open("data.txt", "r") as file:
    # ... read ...
    # اگر اینجا استثنا رخ دهد، file خودکار بسته می‌شود
# file اینجا دیگر بسته شده است
```

**اصل پایتونیک:** همیشه از `with` برای باز کردن فایل استفاده کن — هرگز `f = open()` و `f.close()` دستی.

---

## کار با فایل‌های CSV و JSON

پایتون کتابخانه‌های built-in برای کار با فرمت‌های رایج داده دارد. این یکی از نقاط قوت پایتون نسبت به C++ است که نیاز به کتابخانه خارجی دارد.

### CSV

```python
import csv

# نوشتن CSV
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ali", "25", "Tehran"])

# خواندن CSV به صورت دیکشنری
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']}, lives in {row['City']}")
```

### JSON

```python
import json

# نوشتن JSON
data = {"name": "Ali", "age": 25, "skills": ["Python", "C++"]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# خواندن JSON
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(type(loaded))  # <class 'dict'>
```

---

## استثناها (Exceptions) — مدیریت خطا

### چرا استثناها به‌جای کدهای خطا؟

در C-style programming، توابع کد خطا برمی‌گردانند. این روش سه مشکل اساسی دارد:

۱. **فراموشی بررسی:** هیچ چیز برنامه‌نویس را مجبور نمی‌کند کد خطا را چک کند.

۲. **آلودگی کد:** بعد از هر فراخوانی باید کد خطا چک شود — کد اصلی زیر انبوهی از `if`ها دفن می‌شود.

۳. **نوع خطا مشخص نیست:** کد خطا فقط یک عدد است — نمی‌گوید **چه خطایی** رخ داده.

```python
#[Farsi]
# روش C-style (ناپایتونیک)
def divide(a, b):
    if b == 0:
        return None  # کد خطا
    return a / b

result = divide(10, 0)
if result is None:
    print("Error!")
else:
    print(result + 5)  # اگر فراموش کنی چک کنی، خطا در جای دیگری رخ می‌دهد
```

```python
#[Farsi]
# روش پایتونیک — EAFP (Easier to Ask Forgiveness than Permission)
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
    print(result + 5)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### فلسفه EAFP vs LBYL

پایتون دو فلسفه برای مدیریت خطا دارد:

- **[فارسی] LBYL — Look Before You Leap (اول نگاه کن، بعد بپر):** قبل از عملیات، شرایط را با `if` چک کن. سبک C++ و Java.
- **[فارسی] EAFP — Easier to Ask Forgiveness than Permission (عذرخواهی آسان‌تر از اجازه گرفتن):** عملیات را انجام بده، اگر خطا داد با `except` مدیریت کن. **سبک پایتونیک.**

```python
# LBYL — C-style
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = None

# EAFP — Pythonic
try:
    value = my_dict["key"]
except KeyError:
    value = None
```

**چرا EAFP در پایتون ترجیح داده می‌شود؟**
- در محیط‌های چندنخی (multi-threaded)، بین "look" و "leap" ممکن است شرایط عوض شود (race condition). `try-except` این مشکل را ندارد — عملیات و بررسی خطا **اتمی** (atomic) هستند.
- کد خواناتر است — منطق اصلی از مدیریت خطا جدا می‌شود.
- از validatorهای داخلی پایتون استفاده می‌کند — نیازی به اختراع دوباره چرخ نیست.

### ساختار try-except

```python
try:
    # کدی که ممکن است خطا دهد
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    # اگر ورودی عدد نباشد
    print("That's not a number!")
except ZeroDivisionError:
    # اگر عدد صفر باشد
    print("Cannot divide by zero!")
except Exception as e:
    # هر خطای دیگر
    print(f"Something else went wrong: {e}")
else:
    # فقط اگر هیچ خطایی رخ ندهد
    print(f"Result: {result}")
finally:
    # همیشه اجرا می‌شود — cleanup
    print("Done.")
```

### جدول بخش‌های try-except

| بخش | توضیح | اجباری؟ |
|---|---|---|
| `try:` | کدی که ممکن است خطا دهد | بله |
| `except ErrorType:` | هندل کردن نوع خاصی از خطا | حداقل یکی |
| `except ErrorType as e:` | دسترسی به شیء خطا | اختیاری |
| `else:` | اگر هیچ خطایی رخ ندهد | اختیاری |
| `finally:` | همیشه اجرا می‌شود — cleanup | اختیاری |

### مقایسه با C++

| C++ | Python |
|---|---|
| `try { } catch (T& e) { }` | `try: ... except T as e:` |
| `std::invalid_argument` | `ValueError` |
| `std::out_of_range` | `IndexError` |
| `std::runtime_error` | `RuntimeError` |
| `throw std::runtime_error("msg");` | `raise RuntimeError("msg")` |

### انواع خطاهای رایج در پایتون

| Exception | علت | مثال |
|---|---|---|
| `AttributeError` | attribute یا متد وجود ندارد | `x = 5; x.append(3)` |
| `IndexError` | ایندکس خارج از محدوده | `lst = [1,2,3]; lst[10]` |
| `KeyError` | کلید در dict وجود ندارد | `d = {"a":1}; d["b"]` |
| `TypeError` | نوع اشتباه | `"hello" + 5` |
| `ValueError` | مقدار نامعتبر | `int("hello")` |
| `FileNotFoundError` | فایل وجود ندارد | `open("x.txt", "r")` |

---

## [فارسی] `raise` — پرتاب خطا

[فارسی] `raise` یک شیء Exception ایجاد و پرتاب می‌کند — مانند `throw` در C++. این شیء شامل **نوع خطا** (کلاس) و **پیام خطا** (متن) است.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError(f"Age {age} is unrealistic")
    print(f"Age set to {age}")

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")  # Error: Age 200 is unrealistic
```

**اجزای raise:**
- [فارسی] `ValueError` — نوع خطا (از کلاس Exception ارث‌بری کرده)
- [فارسی] `"Age cannot be negative"` — پیام خطا (برای نمایش یا لاگ)
- [فارسی] `raise` — پرتاب (مثل `throw` در C++)

---

## عملکرد try-except — افسانه یا واقعیت؟

**آیا try-except سرعت کد را کاهش می‌دهد؟** **خیر.** در مسیر عادی (بدون رخداد استثنا)، بلوک `try` **هیچ overhead اضافی** نسبت به کد بدون `try` ندارد. overhead فقط زمانی پرداخت می‌شود که استثنا واقعاً رخ دهد — و استثناها باید **نادر** باشند.

```python
# try-except در مسیر عادی رایگان است
# فقط در صورت رخداد استثنا overhead دارد
# (ساختن stack trace، شیء exception، و stack unwinding)
```

**قانون:** نگران سرعت `try-except` نباش. نگران **خوانایی و درستی** کد باش. استثناها برای شرایط **استثنایی و نادر** طراحی شده‌اند — نه برای جریان عادی برنامه.

---

## الگوی استاندارد — ترکیب Files و Exceptions

```python
def read_file_safely(path):
    """Read file contents. Returns content or None on error."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{path}'.")
        return None
    except UnicodeDecodeError:
        try:
            with open(path, "r", encoding="latin-1") as file:
                return file.read()
        except Exception as e:
            print(f"Error: Encoding issue — {e}")
            return None
```

**نکته:** هرگز `except:` خالی (bare except) ننویس — همه خطاها، از جمله `KeyboardInterrupt` و `SystemExit` را می‌گیرد. همیشه نوع خطا را مشخص کن.

---

## سلسله مراتب استثناها در پایتون

```txt
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    └── RuntimeError

```

[فارسی] `except Exception:` همه چیز زیر `Exception` را می‌گیرد (توصیه: همیشه نوع دقیق‌تر را بگیر).

---

## نکات کلیدی این فصل

1. **همیشه از `with` برای باز کردن فایل استفاده کن.** بسته شدن خودکار حتی در صورت خطا — معادل RAII در C++.

2. **مودهای فایل:** `"r"` (خواندن)، `"w"` (نوشتن)، `"a"` (افزودن)، `"rb"`/`"wb"` (باینری).

3. **پایتون کتابخانه‌های built-in برای CSV و JSON دارد.** برخلاف C++ که نیاز به کتابخانه خارجی دارد.

4. **[فارسی] EAFP بر LBYL ترجیح داده می‌شود.** "عذرخواهی آسان‌تر از اجازه گرفتن" — عملیات را انجام بده، خطا را با `except` بگیر.

5. **[فارسی] `try-except` در مسیر عادی (بدون خطا) overhead ندارد.** overhead فقط در صورت رخداد استثنا پرداخت می‌شود.

6. **همیشه نوع خطا را در `except` مشخص کن.** `except:` خالی خطرناک است — همه چیز را می‌گیرد.

7. **[فارسی] `raise` یک شیء Exception پرتاب می‌کند** — مانند `throw` در C++.

8. **[فارسی] `finally:` برای cleanup استفاده می‌شود** — همیشه اجرا می‌شود، چه خطا رخ دهد چه ندهد.

9. **[فارسی] `else:` در try-except فقط وقتی اجرا می‌شود که هیچ خطایی رخ نداده باشد.**

10. **استثناها را برای جریان عادی برنامه استفاده نکن.** مثلاً `try-except` برای چک کردن "آیا کلید در dict هست؟" مناسب نیست — این کار `if` است. اما برای "فایل باید وجود داشته باشد" عالی است — چون نبودن فایل واقعاً استثنایی است.

---

## پرسش و پاسخ (Q&A)

### سوال: `raise` یعنی متن دلخواه پرتاب کنیم؟
**پاسخ:** خیر. `raise` یک **شیء از نوع Exception** پرتاب می‌کند. متن فقط پیام خطا است. `raise ValueError("msg")` یعنی یک شیء `ValueError` با پیام `"msg"` ساخته و پرتاب می‌شود — معادل `throw std::invalid_argument("msg")` در C++.

### سوال: چرا از try-except استفاده کنیم وقتی می‌شود با if-else هم کار را انجام داد؟
**پاسخ:** if-else برای شرایط **عادی و قابل پیش‌بینی** است. try-except برای شرایط **استثنایی و نادر**. try-except کد را خواناتر می‌کند (جداسازی منطق عادی از خطا)، خطا را نمی‌شود نادیده گرفت، و در محیط‌های چندنخی امن‌تر است (عملیات و بررسی خطا atomic هستند).

### سوال: آیا try-except سرعت اجرا را کاهش می‌دهد؟
**پاسخ:** خیر. در مسیر عادی (بدون رخداد استثنا)، بلوک `try` **هیچ overhead اضافی** نسبت به کد بدون `try` ندارد. overhead فقط در صورت رخداد استثنا پرداخت می‌شود — و استثناها باید نادر باشند.

### سوال: چرا بعضی پروژه‌های C++ از try-catch استفاده نمی‌کنند؟
**پاسخ:** چند دلیل: ۱) در Embedded/Real-time گاهی استثناها با `-fno-exceptions` غیرفعال می‌شوند. ۲) بعضی تیم‌ها از error code pattern یا کلاس Result استفاده می‌کنند. ۳) در C++، استثناها رفتار non-deterministic دارند (stack unwinding). در پایتون، try-except استاندارد و پایتونیک است — overhead کم و خوانایی بالا.

### سوال: EAFP و LBYL یعنی چه؟
**پاسخ:** LBYL (Look Before You Leap) = اول با if چک کن، بعد عمل کن (سبک C++). EAFP (Easier to Ask Forgiveness than Permission) = اول عمل کن، اگر خطا داد با except بگیر (سبک پایتونیک). پایتون EAFP را ترجیح می‌دهد چون خواناتر، امن‌تر در محیط‌های چندنخی، و سازگار با validatorهای داخلی پایتون.