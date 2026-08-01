# ۰۶ - Dictionaries و Sets

## سوال : dict چیست؟

پاسخ : `dict` یک نگاشت کلید به مقدار (key-value mapping) است — معادل `std::unordered_map` در C++.
تفاوت بزرگ: `dict` یک نوع built-in در پایتون است، نه یک کلاس کتابخانه‌ای. سینتکس آن بسیار فشرده‌تر و کار با آن سریع‌تر از C++ است.

**کاربرد در Intelligent Systems:**
- ذخیره‌سازی پیکربندی سیستم (configuration)
- نگاشت شناسه سنسورها به مقادیر آنها
- ساختاردهی داده‌های ورودی/خروجی (مشابه JSON)
- شمارش فرکانس رویدادها

**مقایسه با C++:**

| ویژگی | C++ (`std::unordered_map`) | Python (`dict`) |
|---|---|---|
| ایجاد | `std::unordered_map<std::string, int> m = {{"Ali", 25}};` | `d = {"Ali": 25}` |
| پیاده‌سازی | Hash table | Hash table |
| دسترسی | `m["Ali"]` | `d["Ali"]` |
| دسترسی امن | `m.at("Ali")` — استثنا اگر نباشد | `d.get("Ali")` — None اگر نباشد |
| افزودن | `m["Maryam"] = 28;` | `d["Maryam"] = 28` |
| حذف | `m.erase("Ali");` | `del d["Ali"]` یا `d.pop("Ali")` |
| بررسی وجود | `m.find("Ali") != m.end()` | `"Ali" in d` |
| طول | `m.size()` | `len(d)` |
| comprehension | ندارد | `{k: v for k, v in ...}` |
| اجتماع دو map | دستی (حلقه یا merge) | `d1 \| d2` (Python 3.9+) |

### ایجاد و دسترسی به مقادیر

```python
#i ایجاد dict — معادل std::unordered_map<std::string, int>
ages = {"Ali": 25, "Sara": 30, "Reza": 22}
empty = {}

# دسترسی مستقیم — اگر کلید نباشد KeyError می‌دهد
print(ages["Ali"])  # 25

# دسترسی امن با get() — اگر کلید نباشد None یا مقدار پیش‌فرض برمی‌گرداند
print(ages.get("Unknown"))        # None
print(ages.get("Unknown", "N/A"))  # 'N/A'
```

**نکته:** همیشه برای دسترسی به کلیدهایی که از وجودشان مطمئن نیستی، از `get()` استفاده کن. `d["key"]` اگر کلید نباشد خطا می‌دهد و برنامه متوقف می‌شود. `get()` امن‌تر و Pythonicتر است.

### افزودن، بروزرسانی و حذف

```python
#i افزودن کلید جدید
ages["Maryam"] = 28

# بروزرسانی مقدار کلید موجود
ages["Ali"] = 26

# حذف با del — اگر کلید نباشد KeyError می‌دهد
del ages["Reza"]

# حذف با pop() — مقدار را برمی‌گرداند، اگر کلید نباشد KeyError (یا مقدار پیش‌فرض)
popped = ages.pop("Sara")          # مقدار Sara را برمی‌گرداند
safe = ages.pop("Unknown", None)   # None — بدون خطا
```

**نکته — تفاوت `del` و `pop`:**
- `del d[key]` — فقط حذف می‌کند، مقداری برنمی‌گرداند. سریع‌تر است.
- `d.pop(key)` — حذف می‌کند و مقدار را برمی‌گرداند. وقتی به مقدار حذف‌شده نیاز داری.
- `d.pop(key, default)` — امن‌ترین روش: اگر کلید نباشد، مقدار پیش‌فرض را برمی‌گرداند بدون خطا.

### بررسی وجود کلید و طول

```python
#i بررسی وجود کلید — O(1) average
if "Ali" in ages:
    print("Ali exists")

# طول — تعداد جفت‌های کلید-مقدار
print(len(ages))
```

**نکته:** `in` روی dict کلیدها را بررسی می‌کند، نه مقدارها را. این با C++ که `find()` روی کلیدها کار می‌کند سازگار است.

## پیمایش dict

```python
person = {"name": "Ali", "age": 25, "city": "Tehran"}

# پیمایش کلیدها (پیش‌فرض)
for key in person:
    print(key)

# پیمایش صریح کلیدها
for key in person.keys():
    print(key)

# پیمایش مقدارها
for value in person.values():
    print(value)

# پیمایش جفت‌های کلید-مقدار — رایج‌ترین روش
for key, value in person.items():
    print(f"{key}: {value}")
```

**نکته:** `.items()` رایج‌ترین روش پیمایش dict است. `.keys()` و `.values()` هردو view object برمی‌گردانند — یعنی اگر dict تغییر کند، این viewها هم منعکس می‌شوند.

## dict Comprehension

درست مانند list comprehension هم، dict هم می‌تواند در یک خط ساخته شود:

```python
#[Farsi]
# ساختن dict از یک range
squares = {x: x * x for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# فیلتر با شرط
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# معکوس کردن کلید و مقدار
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

## ادغام dictها

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# عملگر | — Python 3.9+ (مقدارهای d2 جایگزین d1 می‌شوند)
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# روش قدیمی — unpacking
merged_old = {**d1, **d2}
```

## کلیدهای مجاز در dict

**فقط نوع‌های immutable و hashable می‌توانند کلید dict باشند:**
- مجاز: `str`, `int`, `float`, `bool`, `tuple` (اگر همه عناصرش immutable باشند), `None`
- غیرمجاز: `list`, `dict`, `set` — چون mutable هستند و hash ندارند.

```python
#[Farsi]
# کلیدهای معتبر
valid = {42: "int", 3.14: "float", (1, 2): "tuple"}

# کلید نامعتبر — خطا
# invalid = {[1, 2]: "list"}  # TypeError: unhashable type: 'list'
```

**چرا این محدودیت وجود دارد؟** dict از hash table استفاده می‌کند. برای یافتن سریع کلید، باید hash آن محاسبه شود. اگر شیء mutable باشد و تغییر کند، hash آن عوض می‌شود و دیگر در خانه صحیح hash table پیدا نمی‌شود.

## dict و JSON

ساختار JSON و dict تقریباً یکسان هستند. تبدیل بین آنها یک خط است:

```python
import json

# dict -> JSON string
person = {"name": "Ali", "age": 25, "skills": ["Python", "C++"]}
json_string = json.dumps(person, indent=2, ensure_ascii=False)

# JSON string -> dict
parsed = json.loads('{"name": "Sara", "age": 30}')
print(type(parsed))  # <class 'dict'>
```

**نکته:** `json.dumps()` = **D**ump to **S**tring. `json.loads()` = **L**oad from **S**tring. (اگر با فایل کار می‌کنی: `json.dump()` و `json.load()` بدون s)

## مجموعه عناصر یکتا — set

`مجموعه عناصر یکتا — set` مانند `dict` است اما فقط کلید، بدون مقدار. معادل `std::unordered_set` در C++.

**کاربردها:**
- حذف عناصر تکراری از یک لیست
- بررسی عضویت سریع (O(1))
- عملیات مجموعه‌ای (اجتماع، اشتراک، تفاوت)

```python
#[Farsi]
# ایجاد set — دقت: {} خالی dict می‌سازد، نه set
fruits = {"apple", "banana", "cherry"}
empty = set()  # درست — set خالی

# افزودن و حذف
fruits.add("orange")
fruits.remove("banana")   # اگر نباشد KeyError
fruits.discard("mango")   # اگر نباشد، بی‌صدا رد می‌شود
```

**نکته — تفاوت `remove` و `discard`:**
- `s.remove(x)` — اگر `x` نباشد، `KeyError` می‌دهد.
- `s.discard(x)` — اگر `x` نباشد، هیچ اتفاقی نمی‌افتد. امن‌تر برای وقتی که از وجود عنصر مطمئن نیستی.

### عملیات مجموعه‌ای

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # اجتماع (union): {1, 2, 3, 4, 5, 6}
print(a & b)  # اشتراک (intersection): {3, 4}
print(a - b)  # تفاضل (difference): {1, 2}
print(a ^ b)  # تفاضل متقارن (symmetric diff): {1, 2, 5, 6}
```

**مقایسه با C++:**

| عملیات | Python | C++ (`std::unordered_set`) |
|---|---|---|
| ایجاد | `{1, 2, 3}` | `std::unordered_set<int> s = {1, 2, 3};` |
| افزودن | `s.add(4)` | `s.insert(4);` |
| حذف | `s.remove(4)` / `s.discard(4)` | `s.erase(4);` |
| اجتماع | `a \| b` | نیاز به `std::set_union` |
| اشتراک | `a & b` | نیاز به `std::set_intersection` |
| بررسی عضویت | `x in s` | `s.find(x) != s.end()` |

---

## نکات کلیدی این فصل

1. **همیشه از `get()` برای دسترسی امن استفاده کن.** `d[key]` فقط وقتی که از وجود کلید مطمئنی.

2. **تفاوت `del`، `pop`، و `pop` با پیش‌فرض را بشناس.** هر کدام کاربرد خودشان را دارند.

3. **تفاوت `remove` و `discard` در set را به خاطر بسپار.** discard امن‌تر است.

4. **کلیدهای dict باید immutable باشند.** چون از hash table استفاده می‌کند.

5. **`{}` خالی dict می‌سازد، نه set.** برای set خالی باید از `set()` استفاده کنی.

6. **و dict و JSON تقریباً یکی هستند.** تبدیل بین آنها با `json.dumps()` و `json.loads()` انجام می‌شود.

7. **عملیات `|` برای ادغام dictها از Python 3.9 اضافه شده.** در نسخه‌های قدیمی‌تر از `{**d1 و **d2}` استفاده کن.

---

## پرسش و پاسخ (Q&A)

### سوال: فرق `del` و `remove` و `discard` چیست؟
**پاسخ:** `del` برای dict است و کلید را حذف می‌کند بدون برگرداندن مقدار. `remove` برای set است و اگر عنصر نباشد خطا می‌دهد. `discard` برای set است و اگر عنصر نباشد بی‌صدا رد می‌شود.

### سوال: چرا کلید dict باید immutable باشد؟
**پاسخ:** dict با hash table کار می‌کند. اگر کلید mutable باشد و تغییر کند، hash آن عوض می‌شود و دیگر در خانه صحیح hash table پیدا نمی‌شود.

### سوال: چرا `{}` خالی set نمی‌سازد؟
**پاسخ:** چون `{}` از ابتدا برای dict خالی استفاده می‌شده. برای حفظ سازگاری با نسخه‌های قدیمی، set خالی با `set()` ساخته می‌شود.

---

**نکته مهم — `*` و `**` در پایتون:**
این عملگرها ربطی به pointer و reference در C++ ندارند. آنها عملگرهای unpacking هستند:
- `*` — باز کردن iterable (list, tuple, string)
- `**` — باز کردن mapping (dict)

```python
# * — unpack list
numbers = [1, 2, 3]
print(*numbers)  # معادل: print(1, 2, 3)

# ** — unpack dict
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}  # {"a": 1, "b": 2}
```

پایتون اصلاً مفهوم pointer یا reference به سبک C++ ندارد. همه چیز از طریق نام (name) به اشیاء اشاره می‌کند (مدل Name Binding — فصل ۰۲).
Unpacking در آرگومان‌های توابع کاربرد بیشتری دارد که در فصل ۰۸ (Functions) توضیح داده خواهد شد.