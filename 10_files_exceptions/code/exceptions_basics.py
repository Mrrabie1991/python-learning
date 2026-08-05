# 10_files_exceptions/code/exceptions_basics.py
# try-except — Python's exception handling

# ---- Basic try-except ----
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"10 / {num} = {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Something else went wrong: {e}")
else:
    print("No exceptions occurred!")  # فقط اگر خطا رخ ندهد
finally:
    print("This always runs.")  # مثل RAII cleanup