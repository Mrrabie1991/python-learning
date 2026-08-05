# 10_files_exceptions/code/exception_types.py
# Common Python exception types

# AttributeError — attribute یا متد وجود ندارد
# x = 5
# x.append(3)  # AttributeError: 'int' object has no attribute 'append'

# IndexError — ایندکس خارج از محدوده
# lst = [1, 2, 3]
# lst[10]  # IndexError: list index out of range

# KeyError — کلید در dict وجود ندارد
# d = {"a": 1}
# d["b"]  # KeyError: 'b'

# TypeError — نوع اشتباه
# "hello" + 5  # TypeError: can only concatenate str (not "int") to str

# ValueError — مقدار نامعتبر
# int("hello")  # ValueError: invalid literal for int()

# FileNotFoundError — فایل وجود ندارد
# open("nonexistent.txt", "r")  # FileNotFoundError