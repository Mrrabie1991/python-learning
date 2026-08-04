# 08_functions/code/type_hints.py
# Type hints — optional but recommended for readability

# Without type hints
def add_old(a, b):
    return a + b

# With type hints
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

# Complex types — need typing module
from typing import List, Dict, Optional

def get_scores(students: List[str]) -> Dict[str, int]:
    """Return a dict mapping student names to scores."""
    return {name: len(name) * 10 for name in students}

def greet(name: Optional[str] = None) -> str:
    """Greet someone. If name is None, greet 'Guest'."""
    if name is None:
        name = "Guest"
    return f"Hello, {name}!"

# Python does NOT enforce types at runtime
add(3, 5)       # 8
add("Hello ", "World")  # Hello World — works even though we said int!