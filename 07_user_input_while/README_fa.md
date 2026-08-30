# ۰۷ - ورودی کاربر و حلقه while

## گرفتن ورودی از کاربر  — `input()`

 گرفتن ورودی از کاربر  — `input()` در پایتون معادل `std::getline` در C++ است — یک خط کامل از ورودی را می‌خواند و به‌صورت `str` برمی‌گرداند. برخلاف `std::cin >>` که تا اولین whitespace می‌خواند.

**کاربرد در Intelligent Systems:** دریافت فرمان از کاربر، خواندن تنظیمات از کنسول، ارتباط با پروتکل‌های متنی ساده، دریافت پارامترهای پیکربندی در زمان اجرا.

### دریافت ورودی و تبدیل نوع

```python
# input() همیشه str برمی‌گرداند — مثل std::getline در C++
name = input("Enter your name: ")
print(f"Hello, {name}!")

# برای اعداد باید دستی تبدیل کنی — C++: int age = std::stoi(input);
age_str = input("Enter your age: ")
age = int(age_str)
print(f"Next year you will be {age + 1}")

# تبدیل در یک خط
height = float(input("Enter your height (m): "))
print(f"Your height is {height} meters")
```

### مقایسه با C++

| C++ | Python |
|---|---|
| `std::cin >> x;` (تا whitespace) | ندارد — `input()` کل خط را می‌خواند |
| `std::getline(std::cin, s);` | `s = input()` |
| `std::stoi(s)` | `int(s)` |
| `std::stod(s)` | `float(s)` |

**نکته کلیدی:** `input()` همیشه `str` برمی‌گرداند. اگر عدد می‌خواهی، باید دستی تبدیل کنی. این برخلاف `std::cin >> x` است که نوع متغیر را تشخیص می‌دهد و خودکار تبدیل می‌کند.

---

## حلقه `while` — مرور

دستور `while` در پایتون دقیقاً مانند `while` در C++ کار می‌کند: تا وقتی شرط برقرار است، بدنه حلقه اجرا می‌شود.

```python
#[Farsi]
# شمارنده ساده — مثل while در C++
count = 0
while count < 5:
    print(count)
    count += 1

# while با ورودی کاربر — الگوی sentinel
message = ""
while message != "quit":
    message = input("Enter a message (or 'quit' to exit): ")
    if message != "quit":
        print(f"You entered: {message}")
```

---

## الگوی `while True` — جایگزین `do-while`

پایتون `do-while` ندارد. الگوی استاندارد و پایتونیک برای "حداقل یک بار اجرا، سپس بررسی شرط" استفاده از `while True` با `break` است.

```python
# C++ do-while:
# do {
#     x = get_input();
# } while (x < 0);

# Python — while True + break
while True:
    x = int(input("Enter a positive number: "))
    if x > 0:
        break
    print("That's not positive. Try again.")

print(f"You entered: {x}")
```

### چرا این روش پایتونیک است؟

سه روش برای شبیه‌سازی do-while وجود دارد:

```python
#[Farsi]
# روش ۱: while True + break — پایتونیک (صریح و خوانا)
while True:
    x = int(input("Number: "))
    if x > 0:
        break

# روش ۲: متغیر کمکی — شبیه C++، غیرضروری در پایتون
first = True
while first or x <= 0:
    first = False
    x = int(input("Number: "))

# روش ۳: تکرار کد — نقض اصل DRY (Don't Repeat Yourself)
x = int(input("Number: "))
while x <= 0:
    x = int(input("Number: "))
```

**روش ۱ پایتونیک‌تر است چون:**
- قصد برنامه‌نویس را صریح نشان می‌دهد ("تا ابد اجرا کن مگر اینکه break شود").
- شرط خروج دقیقاً همان جایی است که تصمیم گرفته می‌شود، نه در بالای حلقه.
- کد تکراری (duplication) ندارد.

---

## اعتبارسنجی ورودی — الگوی استاندارد

ترکیب `while True` با بررسی شرط، الگوی استاندارد اعتبارسنجی ورودی در پایتون است:

```python
#[Farsi]
# اعتبارسنجی بازه عددی — الگوی استاندارد
while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        break
    print("Out of range. Try again.")

print(f"Valid input: {num}")
```

**مقایسه با C++:**

```cpp
// C++ equivalent
int num;
do {
    std::cout << "Enter a number between 1 and 10: ";
    std::cin >> num;
} while (num < 1 || num > 10);
```

در C++، دستور `do-while` این کار را انجام می‌دهد. در پایتون، `while True + break` جایگزین آن است.

---

## کنترل حلقه  —  `break` و `continue`

دستورات `break` و `continue` در پایتون دقیقاً مشابه C++ عمل می‌کنند:

```python
# break — خروج فوری از حلقه
for i in range(1, 10):
    if i == 5:
        break       # با i=5 از حلقه خارج می‌شود
    print(i)        # 1, 2, 3, 4

# continue — پرش به تکرار بعدی
for i in range(1, 6):
    if i == 3:
        continue    # چاپ برای i=3 رد می‌شود
    print(i)        # 1, 2, 4, 5

# مثال عملی — جمع اعداد تا ورود 0
total = 0
while True:
    num = int(input("Number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Sum: {total}")
```

---

## پردازش لیست با `while` — الگوهای رایج

### جمع‌آوری آیتم‌ها تا رسیدن به Sentinel

```python
#[Farsi]
# جمع‌آوری آیتم‌ها — توقف با مقدار sentinel
items = []
print("Enter items one by one. Enter 'done' to finish.")

while True:
    item = input("Item: ")
    if item.lower() == "done":
        break
    items.append(item)

print(f"You entered {len(items)} items:")
for i, item in enumerate(items, 1):  # enumerate از ۱ شروع می‌کند
    print(f"  {i}. {item}")
```

### حذف عناصر از لیست — چرا `for` خطرناک است؟

```python
#[Farsi]
# روش امن — while با شرط
numbers = [1, 2, 2, 3, 2, 4]
while 2 in numbers:
    numbers.remove(2)  # یک عنصر در هر تکرار حذف می‌شود
print(f"After removing all 2s: {numbers}")  # [1, 3, 4]

# روش ناامن — for (عناصر جا می‌افتند!)
numbers = [1, 2, 2, 3, 2, 4]
for n in numbers:
    if n == 2:
        numbers.remove(n)  # خطر: عنصر بعدی بررسی نمی‌شود
print(f"Buggy result: {numbers}")  # [1, 2, 3, 4] — یک ۲ جا مانده!
```

**چرا `for` خطرناک است؟** وقتی یک عنصر حذف می‌شود، عناصر بعدی یک خانه به عقب جابجا می‌شوند. اما شمارنده داخلی `for` همچنان به ایندکس بعدی می‌رود. عنصری که به جای عنصر حذف‌شده نشسته، دیگر بررسی نمی‌شود. این باگ در C++ با `std::vector` و iterator هم وجود دارد.

**راه‌حل‌های پایتونیک برای حذف عناصر:**

```python
numbers = [1, 2, 2, 3, 2, 4]

# روش ۱: list comprehension — پایتونیک‌ترین
filtered = [n for n in numbers if n != 2]

# روش ۲: while (امن برای حذف تکی)
while 2 in numbers:
    numbers.remove(2)

# روش ۳: پیمایش روی یک کپی
for n in numbers[:]:  # [:] یک کپی سطحی می‌سازد
    if n == 2:
        numbers.remove(n)
```

---

## نکات کلیدی این فصل

1. **تابع `input()` همیشه `str` برمی‌گرداند.** برای اعداد از `int()` یا `float()` استفاده کن.

2. **پایتون `do-while` ندارد.** الگوی استاندارد: `while True` + `break`. این روش صریح، خوانا، و بدون تکرار کد است.

3. **الگوی `while True` + `break` الگوی اصلی اعتبارسنجی ورودی است.** شرط خروج درست در جایی نوشته می‌شود که تصمیم گرفته می‌شود.

4. **هیچ‌وقت در حین پیمایش با `for`، لیست را تغییر نده.** عناصر جابجا می‌شوند و بعضی عناصر از قلم می‌افتند. به‌جای آن از `while`، list comprehension، یا پیمایش روی یک کپی استفاده کن.

5. **برای حذف عناصر تکراری از list comprehension استفاده کن — پایتونیک‌ترین روش است.**

6. **تابع `enumerate(items, 1)` ایندکس را از ۱ شروع می‌کند.** برای نمایش شماره ردیف به کاربر مفید است.

---

## پرسش و پاسخ (Q&A)

### سوال: چرا حذف عنصر در حین `for` باعث جا افتادن عنصر می‌شود؟
**پاسخ:** وقتی عنصری حذف می‌شود، عناصر بعدی یک خانه به عقب جابجا می‌شوند. اما شمارنده داخلی `for` به ایندکس بعدی می‌رود. عنصری که به جای عنصر حذف‌شده نشسته (یعنی عنصر بعدی در لیست قبلی)، دیگر بررسی نمی‌شود. این باگ در C++ با `std::vector` و iterator هم وجود دارد. راه‌حل پایتونیک: list comprehension یا `while`.

### سوال: چرا `while True` از روش‌های دیگر پایتونیک‌تر است؟
**پاسخ:** چون قصد برنامه‌نویس را صریح نشان می‌دهد، شرط خروج درست در جایی است که تصمیم گرفته می‌شود (نه در بالای حلقه)، و کد تکراری ندارد. روش متغیر کمکی یک پرچم غیرضروری اضافه می‌کند، و روش تکرار کد اصل DRY را نقض می‌کند.

### سوال: `try-except` برای اعتبارسنجی ورودی کجای کار می‌آید؟
**پاسخ:** وقتی ورودی باید به عدد تبدیل شود و کاربر ممکن است رشته وارد کند، `try-except ValueError` استفاده می‌شود. این مبحث به‌طور کامل در فصل ۱۰ (Files & Exceptions) تدریس خواهد شد.