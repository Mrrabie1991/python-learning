# ۰۴ - کار با List

## حلقه for در پایتون

### پیمایش عناصر

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

| C++ | Python |
|---|---|
| `for (const auto& item : vec)` | `for item in list:` (فقط خواندنی) |
| `for (auto& item : vec)` | `for i, item in enumerate(list): list[i] = ...` |

### تغییر عناصر list در حلقه

در C++ با `auto&` می‌توان عناصر را مستقیماً تغییر داد. در پایتون:
- برای immutableها (`int`, `str`): باید با `enumerate` و ایندکس تغییر داد.
- برای mutableها (`list`): می‌توان مستقیماً شیء را تغییر داد.

```python
# immutable — نیاز به enumerate
nums = [1, 2, 3]
for i, n in enumerate(nums):
    nums[i] = n * 2
print(nums)  # [2, 4, 6]

# mutable — تغییر مستقیم
matrix = [[1, 2], [3, 4]]
for row in matrix:
    row.append(99)
print(matrix)  # [[1, 2, 99], [3, 4, 99]]
```

**چرا `for fruit in fruits: fruit = ...` کار نمی‌کند؟**
چون `fruit` یک نام (name) است که به شیء اشاره می‌کند. `fruit = ...` نام را rebind می‌کند، نه اینکه عنصر داخل list را تغییر دهد.

### enumerate — پیمایش با ایندکس

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

| C++ | Python |
|---|---|
| `for (int i=0; i < size; i++)` | `for i, item in enumerate(list):` |

### range — حلقه عددی

```python
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)
```

| C++ | Python |
|---|---|
| `for (int i=0; i<n; i++)` | `for i in range(n):` |
| `for (int i=a; i<b; i+=step)` | `for i in range(a, b, step):` |

---

## List Comprehension

در C++، برای ساختن یک بردار جدید از روی بردار دیگر نیاز به حلقه دارید. در پایتون، List Comprehension این کار را در یک خط انجام می‌دهد.

### ساختار

```python
[expression for item in iterable if condition]
```

### مثال‌ها

```python
nums = [1, 2, 3, 4, 5]

# مربع اعداد
squares = [n * n for n in nums]
print(squares)  # [1, 4, 9, 16, 25]

# فیلتر اعداد زوج
evens = [n for n in nums if n % 2 == 0]
print(evens)  # [2, 4]

# if-else در comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# فراخوانی تابع روی عناصر
names = ["ALICE", "BOB"]
lower = [name.lower() for name in names]
print(lower)  # ['alice', 'bob']
```

### حلقه‌های تو در تو (Nested Loops)

```python
colors = ["red", "blue"]
objects = ["car", "bike"]

# ضرب دکارتی — همه با همه
combinations = [f"{c} {o}" for c in colors for o in objects]
print(combinations)  # ['red car', 'red bike', 'blue car', 'blue bike']
```

---

## Tuple — لیست تغییرناپذیر

`tuple` مانند `list` است، با این تفاوت که immutable است. معادل تقریبی `const std::vector` یا `std::array` در C++.

### ایجاد و استفاده

```python
point = (3, 4)
coordinates = 10, 20  # پرانتز اختیاری است
single = (42,)        # ویرگول برای tuple تک‌عنصری الزامی است

print(point[0])  # 3 — ایندکس‌گذاری مانند list
# point[0] = 5   # خطا — tuple immutable است
```

### Unpacking

```python
x, y = point
print(f"x = {x}, y = {y}")  # x = 3, y = 4

# تعویض بدون متغیر موقت
a, b = 1, 2
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 2, b = 1
```

| C++ | Python |
|---|---|
| `std::tie(x, y) = tuple;` | `x, y = point` |
| `std::swap(a, b);` | `a, b = b, a` |

---

## zip — ترکیب متناظر Iterableها

`zip` دو (یا چند) iterable را عنصر به عنصر جفت می‌کند. خروجی آن یک iterator از tupleهاست.

```python
colors = ["red", "blue"]
objects = ["car", "bike"]

# zip — جفت‌کردن متناظر
pairs = [f"{c} {o}" for c, o in zip(colors, objects)]
print(pairs)  # ['red car', 'blue bike']

# zip با سه لیست
names = ["Ali", "Sara"]
ages = [25, 30]
cities = ["Tehran", "Isfahan"]
people = [f"{n}, {a}, {c}" for n, a, c in zip(names, ages, cities)]
print(people)  # ['Ali, 25, Tehran', 'Sara, 30, Isfahan']
```

| هدف | روش |
|---|---|
| ضرب دکارتی (همه با همه) | `[f"{c} {o}" for c in colors for o in objects]` |
| جفت متناظر (یکی به یکی) | `[f"{c} {o}" for c, o in zip(colors, objects)]` |

> **نکته:** `zip` و `enumerate` ابزارهای پیمایش هستند. توضیحات عمیق‌تر این مفاهیم در فصل ۱۳ (Advanced Topics) ارائه خواهد شد.

---

## حلقه while و کنترل حلقه

```python
# while
count = 0
while count < 5:
    print(count)
    count += 1

# break — خروج از حلقه
for n in range(10):
    if n == 5:
        break

# continue — پرش به تکرار بعدی
for n in range(5):
    if n == 2:
        continue
    print(n)
```

---

## پرسش و پاسخ (Q&A)

### سوال: چرا `for fruit in fruits: fruit = fruit.upper()` لیست را تغییر نمی‌دهد؟
**پاسخ:** چون `fruit` یک نام (name) است، نه خود عنصر داخل list. `fruit = ...` نام را به یک شیء جدید rebind می‌کند و ارتباطش با عنصر داخل list قطع می‌شود. برای تغییر عناصر immutable، باید از `enumerate` و ایندکس استفاده کرد. برای عناصر mutable، می‌توان مستقیماً شیء را تغییر داد.

### سوال: تفاوت `zip` و nested loop در list comprehension چیست؟
**پاسخ:** nested loop ضرب دکارتی می‌سازد (همه ترکیب‌های ممکن). `zip` عناصر متناظر را جفت می‌کند (اول با اول، دوم با دوم). برای `zip` از یک `for` با چند متغیر استفاده می‌شود: `for a, b in zip(list1, list2)`.

### سوال: `tuple` کجا کاربرد دارد؟
**پاسخ:** برای داده‌هایی که نباید تغییر کنند — مانند مختصات، رکوردهای کوچک، و کلیدهای dict. همچنین unpacking و swap در پایتون از tuple استفاده می‌کنند.

### سوال: `enumerate` و `zip` چه هستند و کجا بیشتر توضیح داده می‌شوند؟
**پاسخ:** این دو از built-in functionهای پایتون برای کار با iterableها هستند. توضیحات عمیق‌تر در فصل ۱۳ (Advanced Topics) ارائه خواهد شد.