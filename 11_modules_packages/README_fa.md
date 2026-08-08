# ۱۱ - ماژول‌ها، پکیج‌ها و ساختار پروژه

این فصل جواب این سوال را می‌دهد: **"کدهای یک پروژه واقعی را کجا بگذارم که هم خودم بفهمم، هم دیگران، هم ابزارها؟"**

هفت مفهوم اصلی داریم: Module، Import، `if __name__ == "__main__"`، Package، Relative Import، Virtual Environment & pip، Project Structure & pyproject.toml.

---

## ۱.  (ماژول) Module

### چرا ماژول؟

یک فایل ۱۰۰۰ خطی دارید. پیدا کردن یک تابع در آن ۵ دقیقه طول می‌کشد. تغییر یک بخش ممکن است جای دیگر را خراب کند.

**راه‌حل:** کد را به فایل‌های کوچک و مرتبط تقسیم کنید.

### ماژول چیست؟

**یک فایل `.py`.** هیچ چیز بیشتر. هر فایل پایتون خودش یک ماژول است.

**مقایسه با C++:**
- در C++: یک فایل `.cpp` + یک فایل `.h` = یک واحد کد (interface جدا از implementation).
- در Python: یک فایل `.py` = یک ماژول (هم interface، هم implementation).

### ساختن اولین ماژول

فایل `calculator.py`:

```python
# calculator.py
# This file IS a module. Its name is 'calculator'.

PI = 3.14159  # Module-level variable

def add(a, b):
    """Return sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return product of two numbers."""
    return a * b
```

---

## ۲.دستور  Import

### چرا import؟

ماژول `calculator.py` را ساختید. حالا چطور از آن در یک فایل دیگر استفاده کنید؟

### دستور Import چیست؟

دستوری که یک ماژول را **اجرا** می‌کند و از آن یک **شیء module** می‌سازد.

**تفاوت با C++:**
- در سی پلاس پلاس`#include "file.h"` — محتوای فایل را کپی‌پیست می‌کند. هر چیزی که در `file.h` هست، مستقیم در scope فعلی قرار می‌گیرد.
- در پایتون `import module` — فایل `.py` را اجرا می‌کند، یک شیء module می‌سازد، و توابع/متغیرها از طریق آن شیء در دسترس هستند. namespace خودکار ایجاد می‌شود.

### سه روش import

```python
#[Farsi]
# روش ۱: import کل ماژول (پایتونیک‌ترین — همیشه معلوم است هر چیزی از کجا آمده)
import calculator
calculator.add(3, 5)

# روش ۲: import با نام مستعار (برای نام‌های طولانی)
import calculator as calc
calc.add(3, 5)

# روش ۳: import چیزهای خاص (وقتی فقط چند چیز لازم دارید)
from calculator import add, subtract
add(3, 5)  # بدون calculator. — مستقیم در دسترس است

# روش ۴: import همه چیز (ناپایتونیک — namespace را شلوغ می‌کند، استفاده نکنید!)
from calculator import *
```

**اصل پایتونیک:** همیشه `import module` را ترجیح دهید. `from module import *` را فراموش کنید.

---

## ۳. دستور `if __name__ == "__main__"`

### چرا؟

می‌خواهید `calculator.py` را هم بشود **مستقیماً اجرا کرد** (برای تست)، هم بشود **import کرد** (برای استفاده در فایل‌های دیگر). چطور کد تست را فقط در حالت اجرای مستقیم فعال کنید؟

### متغیر `__name__` چیست؟

پایتون برای هر فایل یک متغیر خودکار به اسم `__name__` تعریف می‌کند:

- اگر فایل را **مستقیماً** اجرا کنید (`python calculator.py`) → `__name__` برابر `"__main__"` است.
- اگر فایل **import** شود (`import calculator`) → `__name__` برابر `"calculator"` (نام ماژول) است.

### ساختن

```python
# calculator_with_test.py
# This file can be BOTH imported AND run directly

PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test code — only runs when file is executed directly
if __name__ == "__main__":
    print("Testing calculator module:")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"PI = {PI}")
```

```bash
#[Farsi]
# اجرای مستقیم — کد تست اجرا می‌شود
python calculator_with_test.py

# import — کد تست اجرا نمی‌شود
python -c "import calculator_with_test; print(calculator_with_test.add(2, 3))"
```

---

## ۴. Package

### چرا Package؟

پروژه شما ۲۰ ماژول دارد. همه را در یک پوشه ریخته‌اید. شلوغ است. نمی‌دانید کدام ماژول به کدام بخش پروژه مربوط است.

**راه‌حل:** ماژول‌های مرتبط را در **پوشه‌های جدا** بگذارید. به این پوشه‌ها Package می‌گوییم.

### Package چیست؟

یک **پوشه** که یک فایل `__init__.py` در آن هست. همین.

**مقایسه با C++:**
- C++: `namespace sensors { class Camera { }; }`
- Python: پوشه `sensors/` (package) با فایل `camera.py` (ماژول) داخل آن.

### `__init__.py` چیست؟

فایلی که به پایتون می‌گوید "این پوشه یک package است، می‌توانی importاش کنی."

- می‌تواند **کاملاً خالی** باشد.
- می‌تواند **کد initialization** داشته باشد (مثلاً import کردن زیرماژول‌ها برای دسترسی آسان‌تر).

### ساختار یک Package

```
robot/                  # Package (پوشه)
├── __init__.py         # این فایل پوشه را package می‌کند
├── sensors.py          # Module (فایل .py)
└── navigation.py       # Module (فایل .py)
```

### ساختن

فایل `robot/__init__.py`:

```python
# robot/__init__.py
# This file turns the 'robot' folder into a Python package.

# Re-export commonly used classes for easier access
from .sensors import Camera, Motor

__version__ = "0.1.0"
```

فایل `robot/sensors.py`:

```python
# robot/sensors.py

class Camera:
    def __init__(self, resolution=(1920, 1080)):
        self.resolution = resolution

    def read(self):
        return f"Camera: image at {self.resolution}"

class Motor:
    def __init__(self, max_speed=100):
        self.max_speed = max_speed

    def set_speed(self, speed):
        return f"Motor: speed set to {min(speed, self.max_speed)}"
```

فایل `robot/navigation.py`:

```python
# robot/navigation.py

class PathPlanner:
    def plan(self, start, goal):
        return f"Path planned from {start} to {goal}"

class Localizer:
    def get_position(self):
        return (0, 0)
```

```python
#[Farsi]
# استفاده از package

from robot.sensors import Camera
cam = Camera()
print(cam.read())

from robot import Motor  # re-export شده در __init__.py
motor = Motor()
print(motor.set_speed(50))
```

### `__all__` چیست؟

لیستی از اسم‌ها که تعیین می‌کند وقتی کسی بنویسد `from package import *`، **دقیقاً چه چیزهایی** import شوند. مانند `public:` در C++.

```python
# robot/__init__.py
__all__ = ["Camera", "Motor", "PathPlanner"]

# حالا:
# from robot import * → فقط Camera, Motor, PathPlanner import می‌شوند
```

---

## ۵. Relative Import

### چرا؟

در `robot/navigation.py` می‌خواهید از `robot/sensors.py` استفاده کنید. اگر اسم package را عوض کنید (`robot` → `my_robot`)، importهای مطلق می‌شکنند.

**راه‌حل:** Relative import — نسبت به موقعیت فایل جاری آدرس بدهید.

```python
# robot/navigation.py — با relative import

from .sensors import Camera  # . یعنی همین پوشه (robot/)

class PathPlanner:
    def __init__(self):
        self.camera = Camera()

    def plan(self, start, goal):
        image = self.camera.read()
        return f"Using {image} | Path from {start} to {goal}"
```

### نشانه‌گذاری

| نماد | معنی | مثال |
|---|---|---|
| `.` | همین پوشه (current package) | `from .sensors import Camera` |
| `..` | پوشه والد (parent package) | `from ..utils import helper` |
| `...` | پدربزرگ (grandparent) | `from ...common import config` |

---

## ۶. Virtual Environment & pip

### چرا؟

پروژه A به `numpy==1.21` نیاز دارد. پروژه B به `numpy==1.26`. اگر همه چیز را در سیستم نصب کنید، این دو نسخه باهم تداخل پیدا می‌کنند.

**راه‌حل:** برای هر پروژه یک **محیط ایزوله** (Virtual Environment) بسازید.

**مقایسه با C++:**
- در C++: هر پروژه کتابخانه‌هایش را در پوشه `Dependencies/` یا با Conan/vcpkg مدیریت می‌کند.
- در Python: هر پروژه یک `venv/` دارد که یک کپی ایزوله از پایتون و کتابخانه‌هایش است.

### گام‌به‌گام

```bash
#[Farsi]
# ۱. ساختن محیط مجازی
python -m venv venv

# ۲. فعال‌سازی (Linux / Git Bash)
source venv/bin/activate
# Windows PowerShell:
# .\venv\Scripts\Activate.ps1

# ۳. نصب کتابخانه
pip install requests

# ۴. دیدن کتابخانه‌های نصب‌شده
pip list

# ۵. ذخیره وابستگی‌ها
pip freeze > requirements.txt

# ۶. غیرفعال‌سازی
deactivate

# ۷. بازسازی محیط روی سیستم دیگر
# source venv/bin/activate
# pip install -r requirements.txt
```

### فلسفه

- پوشه `venv/` را **هرگز** در git commit نکنید (در `.gitignore` است).
- فقط `requirements.txt` (یا `pyproject.toml`) را commit کنید.
- هرکس پروژه را clone کند، با `pip install -r requirements.txt` دقیقاً همان محیط را می‌سازد.

---

## ۷. ساختار پروژه استاندارد & pyproject.toml

### چرا؟

یک پروژه واقعی فقط کد نیست. تست دارد، داده دارد، مستندات دارد، وابستگی دارد. همه اینها باید یک جای مشخص باشند. همچنین می‌خواهید پروژه را مثل یک کتابخانه نصب کنید تا از هر جایی import شود.

### ساختار استاندارد

```
my_robot/                    # ریشه پروژه (repository root)
├── src/                     # کد اصلی
│   └── my_robot/            # پکیج پایتون
│       ├── __init__.py      # __version__ اینجاست
│       ├── main.py          # نقطه ورود برنامه
│       ├── core.py          # منطق اصلی
│       ├── sensors/         # پکیج سنسورها
│       │   ├── __init__.py
│       │   ├── camera.py
│       │   └── lidar.py
│       ├── navigation/      # پکیج مسیریابی
│       │   ├── __init__.py
│       │   ├── planner.py
│       │   └── controller.py
│       └── utils.py         # توابع کمکی مشترک
├── tests/                   # تست‌ها (جدا از کد اصلی)
│   ├── __init__.py
│   ├── test_camera.py
│   └── test_planner.py
├── data/                    # فایل‌های داده (نه کد)
├── venv/                    # محیط مجازی (gitignore)
├── .gitignore
├── README.md
├── requirements.txt         # وابستگی‌ها (ساده)
└── pyproject.toml           # پیکربندی پروژه (مدرن)
```

### `pyproject.toml` چیست؟

**شناسنامه پروژه** — جایگزین مدرن چندین فایل قدیمی. یک فایل متنی با فرمت TOML.

**قبلاً:** پروژه‌های پایتون چندین فایل پیکربندی داشتند (`setup.py`, `setup.cfg`, `requirements.txt`).
**الان:** `pyproject.toml` همه اینها را یک‌جا جمع می‌کند.

### بخش‌های اصلی

```toml
#[Farsi]
# بخش ۱: build system — همیشه ثابت، کپی کنید
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

# بخش ۲: project metadata — شناسنامه پروژه
[project]
name = "my_robot"
version = "0.1.0"
description = "A demo robot package"
requires-python = ">=3.9"
dependencies = [
    "numpy>=1.24",
    "requests>=2.28",
]             # کتابخانه‌های مورد نیاز

# بخش ۳: optional dependencies — ابزارهای توسعه
[project.optional-dependencies]
dev = ["pytest>=7.0"]

# بخش ۴: اگر پکیج در پوشه src/ است
[tool.setuptools.packages.find]
where = ["src"]

# بخش ۵: تنظیمات ابزارها
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
```

### راهنمای نوشتن `pyproject.toml`

نوشتن `pyproject.toml` مثل `CMakeLists.txt` در C++ است — یک بار الگو را یاد می‌گیرید، برای هر پروژه جدید فقط `name` و `dependencies` را تغییر می‌دهید.

- **بخش `[build-system]`:** همیشه ثابت است. هر پروژه‌ای همین را دارد.
- **بخش `[project]`:** فقط `name` (اسم پکیج) و `dependencies` (کتابخانه‌های مورد نیاز) را تغییر دهید.
- **بخش `[tool.setuptools.packages.find]`:** اگر پکیج در پوشه `src/` است، این را بگذارید. اگر نیست، حذف کنید.
- **بخش‌های `[tool.*]`:** فقط اگر از آن ابزار استفاده می‌کنید.

### `pip install` و انواع آن

| دستور | کاربرد | رفتار |
|---|---|---|
| `pip install numpy` | نصب کتابخانه عمومی | کپی در site-packages |
| `pip install .` | نصب پروژه برای **استفاده** | کپی در site-packages |
| `pip install -e .` | نصب پروژه برای **توسعه** | لینک به پوشه اصلی — تغییرات زنده |
| `pip install -e .[dev]` | نصب توسعه + ابزارهای dev | مانند بالا + pytest و black |

### `-e` (editable) یعنی چه؟

**بدون `-e`:** پایتون کد پروژه را **کپی** می‌کند در `site-packages/`. اگر کد را تغییر دهید، تغییرات اعمال نمی‌شوند — باید دوباره `pip install` کنید.

**با `-e`:** پایتون **کپی نمی‌گیرد**. یک لینک به پوشه پروژه ایجاد می‌کند. هر تغییری در کد بدهید، **بلافاصله** همه‌جا اعمال می‌شود. مخصوص زمان توسعه.

### `.` یعنی چه؟

`.` = همین پوشه (پوشه‌ای که `pyproject.toml` در آن هست).

### `pip install` و وابستگی‌ها

- `pip install .` ← `pyproject.toml` را می‌خواند، `dependencies` را **خودکار** نصب می‌کند.
- `pip install -r requirements.txt` ← فقط `requirements.txt` را می‌خواند. باید **دستی** اجرایش کنید.
- اگر پروژه `pyproject.toml` داشته باشد، `pip install .` کافی است.

### `[dev]` یعنی چه؟

وابستگی‌های اختیاری. کاربر عادی به pytest نیاز ندارد. فقط توسعه‌دهنده‌ها `[dev]` را نصب می‌کنند.

```bash
pip install -e .            # فقط numpy, requests
pip install -e .[dev]       # numpy, requests + pytest, black
```

### `python -m my_robot.main` یعنی چه؟

اجرای یک **ماژول** (نه فایل). `-m` یعنی module. پایتون `my_robot.main` را در `sys.path` جستجو می‌کند و اجرایش می‌کند.

```bash
#[Farsi]
# اجرای فایل با مسیر
python src/my_robot/main.py

# اجرای ماژول (بعد از pip install -e .)
python -m my_robot.main      # از هر جای سیستم
```

---

## جمع‌بندی

| # | مفهوم | در یک خط | معادل C++ |
|---|---|---|---|
| ۱ | **Module** | یک فایل `.py` | فایل `.cpp` + `.h` |
| ۲ | **Import** | اجرای ماژول و ساختن شیء module | `#include` (طرز کار کاملاً متفاوت) |
| ۳ | **`if __name__ == "__main__"`** | کدی که فقط در اجرای مستقیم اجرا می‌شود | فایل جدا با `main()` |
| ۴ | **Package** | پوشه با `__init__.py` | `namespace` |
| ۵ | **Relative Import** | import نسبت به موقعیت فایل جاری | `#include "../"` |
| ۶ | **venv + pip** | محیط ایزوله + نصب کتابخانه | Conan / vcpkg / Docker |
| ۷ | **pyproject.toml** | شناسنامه پروژه | `CMakeLists.txt` |

---

## پرسش و پاسخ (Q&A)

### سوال: `__all__` چیست و چه می‌کند؟
**پاسخ:** لیستی از اسم‌ها که تعیین می‌کند وقتی کسی بنویسد `from package import *`، دقیقاً چه چیزهایی import شوند. مانند `public:` در C++. فقط روی `from package import *` تأثیر دارد — import مستقیم (مثل `from package import _internal`) همچنان کار می‌کند.

### سوال: `pip install -e .` یعنی چه؟
**پاسخ:** پروژه را در حالت توسعه (editable) نصب می‌کند. `-e` یعنی پایتون کد را کپی نمی‌کند — یک لینک به پوشه اصلی پروژه ایجاد می‌کند. هر تغییری در کد بلافاصله همه‌جا اعمال می‌شود. `.` یعنی همین پوشه (جایی که `pyproject.toml` هست).

### سوال: `[build-system]` در `pyproject.toml` چیست؟
**پاسخ:** به pip می‌گوید برای آماده‌سازی پروژه از چه ابزاری استفاده کند. "آماده‌سازی" یعنی خواندن metadata، کپی (یا لینک) کردن فایل‌ها به `site-packages/`. این build به معنی کامپایل نیست — پایتون کامپایل نمی‌شود.

### سوال: `pip install .` خودش وابستگی‌ها را هم نصب می‌کند؟
**پاسخ:** اگر پروژه `pyproject.toml` داشته باشد، بله — بخش `dependencies` را می‌خواند و خودکار نصب می‌کند. اگر فقط `requirements.txt` داشته باشد، خیر — باید جداگانه `pip install -r requirements.txt` را اجرا کنید.

### سوال: `[dev]` در `pip install -e .[dev]` چیست؟
**پاسخ:** وابستگی‌های اختیاری. در `pyproject.toml`، بخش `[project.optional-dependencies]` تعریف می‌شوند. `dev` معمولاً شامل ابزارهای توسعه (pytest, black, mypy) است. کاربران عادی نیازی به نصب آنها ندارند.

### سوال: `python -m my_robot.main` یعنی چه؟
**پاسخ:** اجرای یک ماژول (نه فایل). `-m` یعنی module. پایتون `my_robot.main` را در `sys.path` جستجو می‌کند. `.main` یعنی ماژول `main.py` داخل پکیج `my_robot/`. بعد از `pip install -e .`، این دستور از هر جای سیستم کار می‌کند.

### سوال: چطور `pyproject.toml` بنویسم؟
**پاسخ:** یک الگوی ثابت دارد. بخش `[build-system]` همیشه ثابت است. بخش `[project]` را با `name` و `dependencies` پروژه خود پر کنید. اگر پکیج در `src/` است، `[tool.setuptools.packages.find]` را اضافه کنید. مثل `CMakeLists.txt` — یک بار یاد بگیرید، بعد کپی کنید.

### سوال: آیا در پایتون هم مثل C++ فایل اجرایی (exe) داریم؟
**پاسخ:** خیر. پایتون فایل `.py` (متن) را مستقیماً اجرا می‌کند. برای توزیع، می‌توان از PyInstaller برای ساخت فایل اجرایی استفاده کرد، یا کد را همان‌طور که هست توزیع کرد. فلسفه پایتون open-source بودن کد است.

### سوال: `__version__ = "0.1.0"` را چرا در `__init__.py` می‌نویسیم؟
**پاسخ:** این یک قرارداد برای ذخیره نسخه پروژه است. `__init__.py` اولین چیزی است که موقع import پکیج اجرا می‌شود، بنابراین `__version__` همیشه در دسترس است: `import my_robot; print(my_robot.__version__)`. ابزارهای خودکار (مثل pip) گاهی نسخه را از اینجا می‌خوانند.