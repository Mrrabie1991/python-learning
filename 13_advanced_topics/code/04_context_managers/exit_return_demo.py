# 13_advanced_topics/code/04_context_managers/exit_return_demo.py

class SuppressErrors:
    """Context manager that swallows all errors (dangerous!)."""

    def __enter__(self):
        print("Entering...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        if exc_type is not None:
            print(f"  Error occurred: {exc_type.__name__}: {exc_val}")
            return True  # Swallow the error — program continues
        return False


class ReraiseErrors:
    """Context manager that lets errors propagate."""

    def __enter__(self):
        print("Entering...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        if exc_type is not None:
            print(f"  Error occurred: {exc_type.__name__}: {exc_val}")
        return False  # Re-raise the error — program stops


# Test 1: SuppressErrors — error is swallowed
print("Test 1: SuppressErrors")
with SuppressErrors():
    x = 1 / 0  # Error occurs but is swallowed
print("  After with block — program continues!\n")

# Test 2: ReraiseErrors — error propagates outside
print("Test 2: ReraiseErrors")
try:
    with ReraiseErrors():
        x = 1 / 0  # Error occurs
except ZeroDivisionError as e:
    print(f"  Caught outside: {e}")