# Sensor Data Analyzer

## تحلیل‌گر داده سنسور

یک ابزار خط فرمان (CLI) پایتون برای تحلیل داده سنسورهای صنعتی از فایل CSV.

این پروژه به عنوان مینی‌پروژه فاز ۱ (Python Foundations) ساخته شده است و مفاهیم زیر را ترکیب می‌کند:

- Classes & OOP (`dataclass`, `@property`)
- File Handling (`with open()`, `csv.DictReader`)
- Exceptions (`try-except`)
- Type Hints (`Optional`, `Any`, `str | Path`)
- List & Dict Comprehension
- Package Structure (`src/`, `pyproject.toml`)
- Testing (`pytest`)

## قابلیت‌ها

- خواندن داده سنسور از فایل CSV
- تشخیص داده‌های نامعتبر (مقادیر خالی یا غیرعددی)
- محاسبه میانگین، بیشینه، و کمینه برای هر فیلد
- نمایش گزارش متنی در ترمینال
- ذخیره گزارش JSON

## نصب

```bash
#[EN]
# ساخت محیط مجازی
python -m venv venv

# فعال‌سازی (Git Bash / Linux)
source venv/Scripts/activate

# نصب پروژه در حالت توسعه
pip install -e .
```

## اجرا

```bash
#[EN]
# نمایش گزارش متنی
python -m sensor_analyzer.cli data/sample_sensors.csv

# ذخیره گزارش JSON
python -m sensor_analyzer.cli data/sample_sensors.csv --json-output output/report.json
```

## اجرای تست‌ها

```bash
pip install pytest
pytest
```

## ساختار پروژه

```
sensor-analyzer/
├── src/
│   └── sensor_analyzer/
│       ├── __init__.py
│       ├── models.py          # کلاس SensorData
│       ├── reader.py          # خواندن CSV
│       ├── analyzer.py        # تحلیل داده
│       ├── reporter.py        # تولید گزارش
│       └── cli.py             # رابط خط فرمان
├── tests/
│   ├── __init__.py
│   ├── test_reader.py
│   ├── test_analyzer.py
│   └── test_reporter.py
├── data/
│   └── sample_sensors.csv     # داده نمونه
├── output/                    # گزارش‌های تولیدشده
├── pyproject.toml
├── README.md
├── README_fa.md
├── .gitignore
└── requirements.txt
```

## خروجی نمونه

```
=== Sensor Data Analysis Report ===

Summary:
  Total readings:   20
  Valid readings:   18
  Invalid readings: 2

Statistics:
  Temperature:
    Average: 27.89
    Max:     33.0
    Min:     22.5
    Count:   19
```

## نکات فنی

- مقادیر نامعتبر در CSV به `None` تبدیل می‌شوند.
- [فارسی] `SensorReading.is_valid` بررسی می‌کند که همه فیلدها عدد معتبر باشند.
- [فارسی] `missing_fields` فیلدهایی که داده نامعتبر دارند را گزارش می‌کند.
- گزارش JSON با `ensure_ascii=False` ذخیره می‌شود تا از کاراکترهای فارسی پشتیبانی کند.