# تمرین‌های فصل ۰۹ — Classes & OOP (Pythonic)

## اهداف تمرین‌ها

این تمرین‌ها برای تثبیت مفاهیم زیر طراحی شده‌اند:

- تعریف کلاس و متد با `self`
- Constructor (`__init__`) و attributeهای نمونه
- Property برای دسترسی کنترل‌شده
- Magic Methods برای operator overloading
- Composition به‌جای Inheritance

## تمرین‌ها

| شماره | عنوان | مفهوم اصلی |
|---|---|---|
| ۹.۱ | کلاس ساده | `class`, متد با `self` |
| ۹.۲ | Constructor و self | `__init__`, attribute نمونه |
| ۹.۳ | Property | `@property`, computed property |
| ۹.۴ | Magic Methods | `__str__`, `__add__`, `__eq__` |
| ۹.۵ | Composition | رابطه has-a |

## نکات کلیدی

- هر متد کلاس باید `self` را به‌عنوان اولین پارامتر بگیرد.
- [فارسی] `self` یعنی "این نمونه خاص" — بدون آن، پایتون نمی‌داند attribute مال کدام نمونه است.
- [فارسی] `@property` تابع را به attribute فقط‌خواندنی تبدیل می‌کند.
- [فارسی] Magic Methods معادل operator overloading در C++ هستند.
- [فارسی] Composition یعنی "یک شیء شامل شیء دیگر است" — انعطاف‌پذیری بیشتر از Inheritance.

## خروجی مورد انتظار

هر فایل باید بدون خطا اجرا شود و خروجی شامل نتایج متدها، propertyها، عملگرها، و رفتار Composition باشد.