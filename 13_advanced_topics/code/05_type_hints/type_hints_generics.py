# 13_advanced_topics/code/05_type_hints/type_hints_generics.py

# Simple types
def add(a: int, b: int) -> int:
    return a + b

# List of integers
def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)

# Dict with string keys and int values
def get_scores() -> dict[str, int]:
    return {"Ali": 85, "Sara": 92}

# Set of strings
def get_tags() -> set[str]:
    return {"python", "testing", "advanced"}

# Tuple with fixed types
def get_coordinates() -> tuple[float, float]:
    return (35.6892, 51.3890)

# Optional — can be int or None
def find_index(items: list[str], target: str) -> int | None:
    """Return index of target, or None if not found."""
    if target in items:
        return items.index(target)
    return None