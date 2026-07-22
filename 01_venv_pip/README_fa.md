# 01 - Virtual Environment & pip

## چی یاد گرفتم؟

Virtual Environment یه محیط ایزوله‌شده برای هر پروژه پایتونه. نمی‌ذاره وابستگی‌های پروژه‌های مختلف با هم قاطی بشن.

## مقایسه با ++C

تو ++C با CMake و پوشه Dependencies وابستگی‌ها رو دستی مدیریت می‌کردم.
تو پایتون، venv این کار رو خودکار انجام میده و یه کپی مجازی از پایتون می‌سازه.

## دستوراتی که یاد گرفتم

### ساختن
```bash
python -m venv venv
```

### فعال‌سازی
```bash
# Linux / macOS / Git Bash on Windows
source venv/bin/activate
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Windows Command Prompt
venv\Scripts\activate.bat
```

### غیرفعال‌سازی
```bash
deactivate
```

### دیدن پکیج‌های نصب‌شده
```bash
pip list
```

## نکات
- پوشه venv/ رو نباید توی Git commit کرد.
- به جاش فایل requirements.txt رو commit می‌کنیم (بعداً یاد می‌گیریم).