# ۱۲ - تست کد (Testing Your Code)

## چرا تست؟

شما یک تابع می‌نویسید، مثلاً `divide(a, b)`. این تابع را در ۱۰ جای مختلف پروژه استفاده می‌کنید. همه چیز کار می‌کند.

۶ ماه بعد، کسی (یا خودتان) می‌آید و این تابع را تغییر می‌دهد. چطور بفهمید که این تغییر، ۱۰ جای دیگر را خراب نکرده است؟

**اگر تست داشته باشید:** دستور `pytest` را می‌زنید. تست fail می‌شود. می‌فهمید که تغییرتان مشکل داشته، قبل از اینکه به دست کاربر برسد.

**اگر تست نداشته باشید:** ۱۰ روز بعد، کاربر می‌گوید "برنامه خروجی اشتباه می‌دهد." نمی‌دانید مشکل از کجاست.

تست یعنی یک تابع دیگر که تابع اصلی را با ورودی‌های مختلف صدا می‌زند و بررسی می‌کند که خروجی همان چیزی است که انتظار دارید.

## Unit Test vs Integration Test

### Unit Test (تست واحد)

**تعریف:** تست کردن **یک تابع** یا **یک کلاس** به تنهایی، بدون هیچ وابستگی به فایل، شبکه، یا دیتابیس.

**هدف:** اگر fail شود، دقیقاً می‌دانید کدام تابع مشکل دارد.

**ویژگی‌ها:** سریع (چند میلی‌ثانیه)، تعداد زیاد (صدها تست)، هر بار که کد را تغییر می‌دهید اجرا می‌شوند.

### Integration Test (تست یکپارچگی)

**تعریف:** تست کردن **چندین ماژول که با هم کار می‌کنند** — مثلاً دوربین + مسیریاب + کنترلر.

**هدف:** اطمینان از اینکه ماژول‌ها وقتی به هم وصل می‌شوند، درست کار می‌کنند.

**ویژگی‌ها:** کندتر (ممکن است به فایل یا شبکه نیاز داشته باشد)، تعداد کم (چندتا)، قبل از commit یا در CI/CD اجرا می‌شوند.

### تفاوت در یک نگاه

| | Unit Test | Integration Test |
|---|---|---|
| چی را تست می‌کند؟ | یک تابع/کلاس | چند ماژول با هم |
| سرعت | خیلی سریع | کندتر |
| تعداد | زیاد | کم |
| خطا | دقیقاً می‌دانید کجاست | نمی‌دانید کدام ماژول |
| ابزار | pytest | pytest (همان ابزار) |
| وابستگی | هیچ | ممکن است فایل/دیتابیس/شبکه |

---

## [فارسی] pytest از صفر

### [فارسی] pytest چیست؟

یک **framework تست** برای پایتون. Framework یعنی مجموعه‌ای از قوانین و ابزارها که تست‌هایتان را بر اساس آنها می‌نویسید و اجرا می‌کنید.

**مقایسه با C++:**
- در C++: Google Test (gtest) — باید کامپایل کنید، فایل اجرایی بسازید، رجیستر کنید.
- در Python: pytest — فقط یک فایل `.py` می‌نویسید و دستور `pytest` را می‌زنید.

### [فارسی] pytest چطور تست‌ها را پیدا می‌کند؟

[فارسی] pytest به صورت خودکار فایل‌ها و توابع تست را بر اساس **قرارداد نام‌گذاری** پیدا می‌کند:

- **فایل‌های تست:** باید با `test_` شروع شوند یا با `_test` تمام شوند.
- **توابع تست:** باید با `test_` شروع شوند.
- **کلاس‌های تست:** باید با `Test` شروع شوند.

هیچ رجیستری لازم نیست. pytest خودش همه چیز را پیدا می‌کند.

### اولین تست

```python
# calculator.py — کدی که می‌خواهیم تست کنیم

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_calculator.py — تست‌ها

from calculator import add, divide
import pytest

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5       # اگر این درست نباشد، تست fail می‌شود
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Test that divide raises ValueError on zero division."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

```bash
pytest
# خروجی: 3 passed in 0.03s
# هر نقطه (.) یعنی یک تست پاس شده
# F = fail, E = error (استثنای پیش‌بینی‌نشده)
```

### دستور assert چیست؟

یک دستور پایتون که یک شرط را بررسی می‌کند. اگر شرط `True` باشد، هیچ اتفاقی نمی‌افتد. اگر `False` باشد، `AssertionError` پرتاب می‌کند و تست fail می‌شود.

```python
assert add(2, 3) == 5   # True → تست ادامه پیدا می‌کند
assert add(2, 3) == 10  # False → تست fail می‌شود
```

**فرق با C++:**
- C++: `EXPECT_EQ(add(2, 3), 5);` — ماکروی gtest
- Python: `assert add(2, 3) == 5` — دستور built-in خود پایتون

### [فارسی] pytest.raises چیست؟

وقتی می‌خواهید تست کنید که یک تابع **باید** استثنا پرتاب کند:

```python
def test_divide_by_zero():
    with pytest.raises(ValueError):     # انتظار دارم ValueError پرتاب شود
        divide(10, 0)                   # این خط باید ValueError بدهد

    # اگر divide استثنا ندهد → تست fail
    # اگر divide استثنای دیگری بدهد → تست fail
    # اگر divide ValueError بدهد → تست پاس
```

---

## داده مشترک برای تست‌ها — Fixture

### مسئله: کد تکراری در تست‌ها

فرض کنید کلاس `Robot` برای تست نیاز به `Camera` دارد. بدون fixture، باید در هر تست Camera را دستی بسازید — کد تکراری.

### راه‌حل: Fixture

[فارسی] Fixture یک تابع کمکی است که **داده یا شیء مورد نیاز** را یک بار می‌سازد و pytest خودش به تست‌ها پاس می‌دهد.

```python
import pytest

@pytest.fixture
def robot():
    """یک Robot آماده برای تست می‌سازد."""
    cam = Camera(resolution=(1920, 1080))
    return Robot(cam)

# تست‌ها robot را به عنوان پارامتر می‌گیرند
def test_robot_move(robot):
    assert robot.move() == "Moving"

def test_robot_stop(robot):
    assert robot.stop() == "Stopped"
```

### [فارسی] pytest چطور fixture را پاس می‌دهد؟

۱. [فارسی] pytest می‌بیند تابع `test_robot_move` پارامتری به اسم `robot` دارد.

۲. می‌گردد ببیند fixtureای به اسم `robot` تعریف شده یا نه.

۳. پیدا می‌کند — `@pytest.fixture` روی تابع `robot()`.

۴. تابع `robot()` را **صدا می‌زند**.

۵. مقداری که `return` می‌کند (شیء Robot) را می‌گیرد.

۶. آن مقدار را به‌عنوان آرگومان `robot` به تابع تست پاس می‌دهد.


**این مکانیزم Dependency Injection نام دارد.** pytest از روی **اسم پارامتر**، fixture را پیدا می‌کند. برای همین اسم باید **دقیقاً یکی** باشد.

### [فارسی] yield در fixture — Setup و Cleanup

[فارسی] `yield` به fixture اجازه می‌دهد هم **قبل از تست** کاری انجام دهد (setup)، هم **بعد از تست** (cleanup). هر چیز قبل از `yield` هست setup است و قبل از تست اجرا می‌شود. هر چیز بعد از `yield` هست cleanup است و بعد از تست اجرا می‌شود.

**نکته:** `yield` جزو مبحث Generatorهاست که در فصل ۱۳ (Advanced Topics) عمیقاً تدریس خواهد شد. در این فصل، فقط کاربرد آن در fixture را ببینید.

```python
@pytest.fixture
def database():
    # Setup — قبل از تست
    db = Database("test_config.json")
    db.connect()
    
    yield db  # ← تست اینجا اجرا می‌شود. db به تست پاس داده می‌شود.
    
    # Cleanup — بعد از تست
    db.disconnect()
    db.delete_all()
```

### Scope fixture — چند بار ساخته شود؟

| Scope | چند بار ساخته می‌شود | کاربرد |
|---|---|---|
| `function` | برای هر تست (پیش‌فرض) | داده‌های ایزوله |
| `class` | برای هر کلاس تست | داده مشترک بین تست‌های یک کلاس |
| `module` | برای هر فایل تست | تنظیمات مشترک |
| `session` | یک بار برای کل session | دیتابیس، شبکه |

```python
@pytest.fixture(scope="function")   # پیش‌فرض
def fresh_list():
    return []

@pytest.fixture(scope="module")     # یک نمونه برای همه تست‌های این فایل
def shared_config():
    return {"timeout": 10}
```

---

## یک تست، چندین ورودی — Parametrize

وقتی چندین تست دارید که فقط ورودیشان فرق می‌کند، به‌جای نوشتن تست‌های تکراری، از `parametrize` استفاده کنید.

```python
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),        # a=2, b=3, expected=5
    (-2, -3, -5),     # a=-2, b=-3, expected=-5
    (0, 5, 5),        # a=0, b=5, expected=5
    (100, 200, 300),  # a=100, b=200, expected=300
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

این تست **۴ بار** اجرا می‌شود — هر tuple یک بار. `@pytest.mark.parametrize` باید **دقیقاً قبل از تابع تست** بیاید، چون یک دکوریتور (decorator) است و قواعد دکوریتورهای پایتون این را الزامی می‌کند.

```python
#[Farsi]
# تست exception با parametrize
@pytest.mark.parametrize("a, b", [
    (10, 0),
    (0, 0),
    (-5, 0),
])
def test_divide_by_zero(a, b):
    """For all inputs, divide should raise ValueError."""
    with pytest.raises(ValueError):
        divide(a, b)
```

---

## برچسب روی تست‌ها — Markers

[فارسی] Markers برچسب‌هایی هستند که به تست می‌چسبانید. سه کاربرد اصلی دارند:

### ۱. دسته‌بندی تست‌ها

بعضی تست‌ها سریع هستند (باید هر دقیقه اجرا شوند). بعضی کند هستند (فقط قبل از commit اجرا شوند).

```python
@pytest.mark.slow
def test_heavy_computation():
    result = sum(range(10_000_000))
    assert result > 0

@pytest.mark.fast
def test_quick_check():
    assert 1 + 1 == 2
```

```bash
pytest -m fast           # فقط fast
pytest -m "not slow"     # همه به جز slow
```

### ۲. [فارسی] Skip کردن تست

وقتی تستی هنوز آماده نیست، یا فقط روی یک سیستم‌عامل خاص کار می‌کند.

```python
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
def test_linux_feature():
    pass
```

### ۳. [فارسی] Expected Failure (شکست مورد انتظار)

وقتی یک باگ را می‌شناسید و قرار است بعداً درستش کنید. تست اجرا می‌شود — اگر fail شود، زرد (warning) نشان داده می‌شود. اگر پاس شود، سبز (XPASS) — یعنی باگ حل شده است.

```python
@pytest.mark.xfail(reason="Known bug #1234")
def test_known_bug():
    assert 1 + 1 == 3  # می‌دانیم fail می‌شود
```

---

## پوشش تست — Coverage

یک معیار که نشان می‌دهد **چند درصد از خطوط کدتان تست شده است.**

```bash
pip install pytest-cov
pytest --cov=calculator
# خروجی: calculator.py  12 lines   83% covered
```

اگر coverage پایین باشد، یعنی بخش‌هایی از کد هستند که هیچ تستی رویشان اجرا نشده. اگر کسی آن بخش‌ها را تغییر دهد، تست‌ها fail نمی‌شوند — ولی باگ وارد سیستم می‌شود.

در CI/CD معمولاً آستانه تعیین می‌شود:

```bash
pytest --cov=my_package --cov-fail-under=80
# اگر coverage زیر ۸۰٪ باشد، CI fail می‌شود
```

---

## نکات تکمیلی

### [فارسی] Fixtureهای مشترک — conftest.py

[فارسی] Fixtureهایی که چندین فایل تست از آنها استفاده می‌کنند را در `conftest.py` قرار دهید. pytest خودکار آنها را پیدا می‌کند — بدون نیاز به import.

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Ali", "age": 25}
```

```python
# tests/test_calculator.py
def test_with_data(sample_data):   # بدون import — خودکار پیدا می‌شود
    assert sample_data["name"] == "Ali"
```

### فایل موقت برای تست — tmp_path

هنگامی که تست نیاز به فایل دارد، از `tmp_path` (fixture داخلی pytest) استفاده کنید. فایل بعد از تست خودکار پاک می‌شود.

```python
def test_write_file(tmp_path):
    file = tmp_path / "test_output.txt"
    file.write_text("Hello, pytest!")
    assert file.read_text() == "Hello, pytest!"
```

### جایگزین کردن توابع — monkeypatch

هنگامی که تابع به چیزهای خارجی (زمان، شبکه، ورودی کاربر) وابسته است، از `monkeypatch` برای جایگزین کردن آنها استفاده کنید.

```python
def test_get_greeting_morning(monkeypatch):
    class MockDateTime:
        @staticmethod
        def now():
            return datetime(2026, 1, 1, 9, 0, 0)
    
    monkeypatch.setattr("datetime.datetime", MockDateTime)
    assert get_greeting() == "Good morning"
```

### [فارسی] capsys — تست خروجی print

برای تست کردن محتوایی که یک تابع print می‌کند.

```python
def test_greet_output(capsys):
    greet("Ali")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Ali!\n"
```

### الگوی نوشتن تست — Arrange-Act-Assert (AAA)

هر تست خوب سه بخش دارد:

```python
def test_withdraw():
    # Arrange (آماده‌سازی): داده‌ها را بسازید
    account = BankAccount(balance=100)
    
    # Act (عمل): کاری که می‌خواهید تست کنید
    result = account.withdraw(30)
    
    # Assert (بررسی): نتیجه باید همان چیزی باشد که انتظار دارید
    assert result == 70
    assert account.balance == 70
```

---

## مقایسه با C++ (Google Test)

| C++ (gtest) | Python (pytest) |
|---|---|
| `TEST(Suite, Name) { }` | `def test_name():` |
| `EXPECT_EQ(a, b);` | `assert a == b` |
| `SetUp()` / `TearDown()` | Fixture با `yield` |
| `TEST_P` + `INSTANTIATE_TEST_SUITE_P` | `@pytest.mark.parametrize` |
| `GTEST_SKIP()` | `@pytest.mark.skip` |
| باید کامپایل کنید، فایل اجرایی بسازید | `pytest` |
| کشف تست دستی (register) | کشف خودکار (قرارداد نام‌گذاری) |

---

## پرسش و پاسخ (Q&A)

### سوال: Unit Test و Integration Test چه فرقی دارند؟
**پاسخ:** Unit Test یک تابع/کلاس را در انزوا تست می‌کند — سریع، زیاد، و دقیق. Integration Test چندین ماژول را با هم تست می‌کند — کندتر، کم، و برای اطمینان از کارکرد کلی سیستم. هر دو با pytest نوشته می‌شوند.

### سوال: pytest چطور fixture را به تست پاس می‌دهد؟
**پاسخ:** pytest از روی **اسم پارامتر** تابع تست، fixture همنام را پیدا می‌کند. تابع fixture را صدا می‌زند، مقدار بازگشتی را می‌گیرد، و به‌عنوان آرگومان به تست پاس می‌دهد. این مکانیزم Dependency Injection نام دارد.

### سوال: `yield` در fixture یعنی چه؟
**پاسخ:** `yield` به fixture اجازه می‌دهد هم **قبل از تست** کاری کند (setup — کد قبل از yield)، هم **بعد از تست** (cleanup — کد بعد از yield). `yield` مقدار را به تست پاس می‌دهد و تابع را معلق می‌کند. بعد از اتمام تست، ادامه تابع fixture اجرا می‌شود. توضیح کامل `yield` و Generatorها در فصل ۱۳ (Advanced Topics) خواهد آمد.

### سوال: Scope fixture چیست؟
**پاسخ:** تعیین می‌کند fixture چند بار ساخته شود. `function` (پیش‌فرض) برای هر تست یک نمونه جدید. `module` یک نمونه برای همه تست‌های یک فایل. `session` یک نمونه برای کل session تست. در پروژه‌های واقعی کاربرد آن را بیشتر خواهید دید.

### سوال: `parametrize` چرا باید پشت سر هم بیاید؟
**پاسخ:** `@pytest.mark.parametrize` یک دکوریتور (decorator) است و قواعد پایتون می‌گوید دکوریتور باید دقیقاً قبل از تابعی که تزئین می‌کند بیاید. این قانون خود زبان پایتون است.

### سوال: `pytest.raises` چطور کار می‌کند؟
**پاسخ:** بررسی می‌کند که آیا کد داخل بلوک `with`، استثنای مورد نظر را پرتاب می‌کند یا نه. اگر پرتاب کند → تست پاس. اگر پرتاب نکند یا استثنای دیگری پرتاب کند → تست fail.

### سوال: تفاوت `skip` و `xfail` چیست؟
**پاسخ:** `skip` تست را اصلاً اجرا نمی‌کند. `xfail` تست را اجرا می‌کند — اگر fail شود، زرد (warning) نشان می‌دهد (منتظرش بودیم). اگر پاس شود، سبز (XPASS) نشان می‌دهد — یعنی باگ احتمالاً حل شده است.