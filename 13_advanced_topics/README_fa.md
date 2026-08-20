# ۱۳ - مباحث پیشرفته (Advanced Topics)

این فصل جمع‌بندی مفاهیمی است که در طول فاز ۱ به آنها اشاره شد و نیاز به توضیح عمیق‌تر داشتند. بدون این مفاهیم، درک کدهای حرفه‌ای پایتون و کتابخانه‌های اصلی ممکن نیست.

مباحث این فصل: Iterator Protocol، Generator & `yield`، Decorator، Context Manager، Type Hints پیشرفته، Concurrency (threading/async/multiprocessing)، و ابزارهای پیمایش (`zip`, `enumerate`, `map`, `filter`).

---

## پایه تمام حلقه‌های پایتون — Iterator Protocol

هر شیئی که بخواهد در `for x in thing` قابل استفاده باشد، باید از این پروتکل پیروی کند:

- [فارسی]`__iter__()` — خود شیء (یا یک iterator) را برگرداند.
- [فارسی]`__next__()` — عنصر بعدی را برگرداند. وقتی عنصر تمام شد، `StopIteration` پرتاب کند.

پشت صحنه، `for` دقیقاً همین دو متد را صدا می‌زند:

```python
numbers = [1, 2, 3]
it = iter(numbers)      # __iter__()
print(next(it))         # __next__() → 1
print(next(it))         # __next__() → 2
print(next(it))         # __next__() → 3
# next(it) → StopIteration
```

**[فارسی] Iterable vs Iterator:**
- **[فارسی] Iterable:** هر شیئی که `__iter__` دارد (list, dict, set, str, range). می‌توان روی آن `for` زد.
- **[فارسی] Iterator:** شیئی که هم `__iter__` دارد، هم `__next__` (مثل `iter(list)`). کار واقعی پیمایش را انجام می‌دهد.

**[فارسی] `range` یک Sequence است، نه Iterator ساده.** اعداد را ذخیره نمی‌کند — با فرمول `start + index * step` در لحظه محاسبه می‌کند. به همین دلیل `len()` و ایندکس‌دهی روی آن O(1) است و حافظه آن ثابت (چند بایت) می‌ماند.

---

## [فارسی] Generator & `yield`

### مسئله

پردازش داده‌های بزرگ (فایل ۱۰ گیگابایتی، جریان بی‌نهایت) بدون بارگذاری همه در حافظه.

### راه‌حل: `yield`

کلمه `yield` یک تابع معمولی را به **Generator** تبدیل می‌کند. Generator یک Iterator است که:

- هر `next()` آن را از همان جایی که مکث کرده بود ادامه می‌دهد (نه از اول).
- وضعیت داخلی (متغیرهای محلی) را بین فراخوانی‌ها حفظ می‌کند.
- هر بار فقط یک مقدار تولید می‌کند — حافظه ثابت.

```python
def count_up_to(n):
    """Generate numbers from 1 to n, one at a time."""
    i = 1
    while i <= n:
        yield i    # Return i and pause
        i += 1

g = count_up_to(3)   # generator object — function does NOT execute yet
print(next(g))       # 1 — executes to first yield
print(next(g))       # 2 — resumes from after previous yield
print(next(g))       # 3
# next(g) → StopIteration
```

### تفاوت `return` و `yield`

- [فارسی] `return` — تابع تمام می‌شود. همه چیز یکباره محاسبه می‌شود.
- [فارسی] `yield` — تابع مکث می‌کند. عنصر بعدی فقط وقتی `next()` صدا زده شود محاسبه می‌شود.

### چرا Generator؟

وقتی با داده‌های بزرگ کار می‌کنی، Generator فقط عنصر فعلی را در حافظه نگه می‌دارد. در C++ سنتی معادل آن نوشتن یک کلاس کامل با وضعیت داخلی و `operator()()` است — پایتون این را خودکار انجام می‌دهد.

---

## [فارسی] Decorator

### مسئله

افزودن رفتار مشترک (لاگ، زمان‌سنجی، بررسی دسترسی) به چندین تابع بدون تکرار کد.

### راه‌حل: Decorator

[فارسی] Decorator تابعی است که تابع دیگری را می‌گیرد، رفتار جدیدی به آن اضافه می‌کند، و تابع جدید برمی‌گرداند.

```python
def measure_time(func):
    """Measure and print execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(1.5)
    return "Done"

# @measure_time یعنی: slow_function = measure_time(slow_function)
```

[فارسی] Decoratorهایی که در طول فاز ۱ استفاده شدند: `@property`, `@staticmethod`, `@classmethod`, `@pytest.fixture`, `@pytest.mark.parametrize`.

---

## [فارسی] Context Manager (`with`)

### مسئله

مدیریت منابع (فایل، دیتابیس، قفل) به طوری که همیشه آزاد شوند — حتی اگر خطا رخ دهد.

### راه‌حل: Context Manager

[فارسی] `with` یک میانبر نحوی برای `try-finally` است. هر کلاسی که دو متد زیر را داشته باشد، با `with` کار می‌کند:

- [فارسی] `__enter__` — موقع ورود به بلوک `with`.
- [فارسی] `__exit__` — موقع خروج (همیشه اجرا می‌شود، حتی با خطا).

```python
class Timer:
    """Measure execution time of a code block."""
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Elapsed: {time.time() - self.start:.4f}s")
        return False  # Re-raise any exception

with Timer() as t:
    # Code to measure
    sum(range(10_000_000))
```

**مقایسه با C++:** معادل Context Manager در C++ همان RAII است — constructor/destructor. تفاوت کلیدی: `__exit__` زمان اجرایش دقیق و تضمینی است، در حالی که destructor پایتون (`__del__`) زمان اجرایش نامشخص است.

[فارسی] `return False` در `__exit__` یعنی "خطا را دوباره پرتاب کن" (پیش‌فرض امن). `return True` یعنی "خطا را خفه کن" (نادر و خطرناک).

---

## [فارسی] Type Hints پیشرفته

[فارسی] Type Hints در پایتون **هیچ اجباری ایجاد نمی‌کنند** — مفسر آنها را کاملاً نادیده می‌گیرد. فقط ابزارهای static analysis (مثل mypy یا Pyright) آنها را بررسی می‌کنند.

### انواع پرکاربرد

```python
def process(
    numbers: list[int],
    scores: dict[str, int],
    point: tuple[float, float],
    maybe: int | None,
) -> str:
    ...
```

### Protocol — تایپ ساختاری (Duck Typing رسمی)

```python
from typing import Protocol

class Readable(Protocol):
    def read(self) -> str: ...

def process_data(source: Readable) -> str:
    return source.read()
```

هر کلاسی که `read()` داشته باشد قابل قبول است — بدون نیاز به ارث‌بری مشترک.

### Callable — تابع به عنوان پارامتر یا خروجی

```python
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))
```

### TypedDict — دیکشنری با ساختار مشخص

```python
from typing import TypedDict

class RobotConfig(TypedDict):
    camera_resolution: tuple[int, int]
    max_speed: int
    sensors: list[str]
```

### Literal — فقط مقادیر مشخص

```python
from typing import Literal

def set_robot_status(status: Literal["start", "stop", "pause"]) -> str:
    ...
```

---

## آشنایی — Concurrency

[فارسی] `GIL` مخفف  (Global Interpreter Lock)

پایتون (CPython) یک قفل سراسری دارد که اجازه می‌دهد در هر لحظه فقط یک Thread کد پایتون را اجرا کند. این قفل هر ۵ میلی‌ثانیه بین Threadها جابجا می‌شود.

[فارسی] `I/O-bound vs CPU-bound`

· [فارسی] `I/O-bound`: منتظر ماندن برای شبکه، فایل، دیتابیس. GIL موقع انتظار آزاد می‌شود — Thread عالی کار می‌کند.

· [فارسی] `CPU-bound`: محاسبات سنگین. GIL هی آزاد نمی‌شود — Thread فایده ندارد.

### راه‌حل‌ها

| کار  | راه‌حل |
|---|---|
| I/O-bound | `asyncio` (مدرن) or `threading` |
| CPU-bound | `multiprocessing` (چند مفسر پایتون جداگانه) |
| I/O + CPU | ترکیب `asyncio` + `multiprocessing` |


### [فارسی] Async/Await

[فارسی] `async def` یک coroutine function می‌سازد. `await` یعنی "من اینجا منتظر می‌مانم، event loop برو کارهای دیگر انجام بده." ورود به دنیای async با `asyncio.run(main())` است.

```python
async def download_file(file_id: int) -> str:
    await asyncio.sleep(1)
    return f"file_{file_id}.dat"

async def main():
    tasks = [download_file(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    return results

asyncio.run(main())
```

قانون: هر تابعی که await دارد باید async def باشد. توابع sync (محاسبات خالص) معمولی می‌مانند و فقط بخش I/O  ها async می‌شوند.

نکته: Concurrency در پایتون در فازهای بعدی (پروژه‌های واقعی با شبکه، سنسورها، رباتیک) عمیقاً بررسی خواهد شد. اینجا فقط آشنایی مفهومی است.

---

## ابزارهای پیمایش: `zip, enumerate, map, filter`

این چهار تابع همگی Iterator برمی‌گردانند — عناصر را در لحظه تولید می‌کنند، نه اینکه لیست جدید بسازند.

zip — جفت کردن عناصر متناظر

```python
names = ["Ali", "Sara", "Reza"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

#ساختن dict

person = dict(zip(["name", "age"], ["Ali", 25]))

#Transpose ماتریس

transposed = list(zip(*matrix))
```

enumerate — ایندکس و مقدار

```python
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
```

map — اعمال تابع روی هر عنصر

```python
result = map(lambda x: x * x, numbers)  # Iterator

```

**نکته:** برای lambda، معمولاً list comprehension خواناتر است:

```python
result = [x * x for x in numbers]
```

### `filter` — نگه داشتن عناصر بر اساس شرط

```python
result = filter(lambda x: x % 2 == 0, numbers)  # Iterator
# پایتونیک‌تر:
evens = [x for x in numbers if x % 2 == 0]
```

### قانون کلی

- `zip` و `enumerate` — همیشه استفاده کن.
- `map` و `filter` با تابع نام‌دار — خوبند.
- `map` و `filter` با lambda — list comprehension بهتر است.

---

## جمع‌بندی

| مفهوم | در یک خط | معادل C++ |
|---|---|---|
| Iterator Protocol | `__iter__` + `__next__` | `begin()`, `end()`, `operator++` |
| Generator | تابعی که `yield` می‌کند | C++20 coroutines (`co_yield`) |
| Decorator | تابعی که تابع می‌گیرد و تابع برمی‌گرداند | Higher-order functions / lambda |
| Context Manager | `__enter__` + `__exit__` | RAII (constructor/destructor) |
| GIL | قفل سراسری — یک Thread در لحظه | — (چنین محدودیتی ندارد) |
| Async | event loop + coroutine | C++20 coroutines |
| `zip` / `map` / `filter` | Iteratorهای پیمایش | `std::views` (C++20/23) |

---

## پرسش و پاسخ (Q&A)

### سوال: چرا `range` حافظه اشغال نمی‌کند ولی `len` و ایندکس دارد؟
**پاسخ:** `range` یک Sequence است، نه Iterator ساده. اعداد را با فرمول `start + index * step` در لحظه محاسبه می‌کند. `len` و ایندکس‌دهی O(1) هستند چون فقط محاسبه ریاضی‌اند، نه پیمایش.

### سوال: `yield` در fixture تست چطور کار می‌کند؟
**پاسخ:** `yield` تابع را به Generator تبدیل می‌کند. pytest با `next()` اول، کد قبل از `yield` (setup) را اجرا می‌کند، مقدار را می‌گیرد، تست را اجرا می‌کند، سپس با `next()` دوم، کد بعد از `yield` (cleanup) را اجرا می‌کند.

### سوال: `return False` و `return True` در `__exit__` یعنی چه؟
**پاسخ:** `return False` (پیش‌فرض) یعنی "خطا را دوباره پرتاب کن." `return True` یعنی "خطا را خفه کن" — برنامه ادامه می‌دهد. در ۹۹٪ مواقع `return False` درست است.

### سوال: GIL چرا طراحی شده؟
**پاسخ:** دلیل تاریخی — مدیریت حافظه پایتون (Reference Counting) thread-safe نبود. ساده‌ترین راه، گذاشتن یک قفل سراسری بود. این قفل برای I/O-bound آزاد می‌شود، اما CPU-bound را محدود می‌کند. راه‌حل: `multiprocessing` (چند مفسر جداگانه).

### سوال: Async و Thread چه فرقی دارند؟
**پاسخ:** Thread = چند کارگر که هر کدام کار خودشان را می‌کنند (با GIL مشترک). Async = یک کارگر که بین کارها می‌پرد (event loop). Async سربار کمتری دارد و برای I/O-bound مدرن‌تر و پایتونیک‌تر است.

### سوال: چرا `map` و `filter` با lambda توصیه نمی‌شوند؟
**پاسخ:** چون list comprehension خواناتر و صریح‌تر است. `[x * x for x in numbers]` واضح‌تر از `map(lambda x: x * x, numbers)` است. برای توابع نام‌دار، `map` و `filter` قابل قبول‌اند.