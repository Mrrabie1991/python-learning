# test_calculator.py — tests for calculator.py

from calculator import add, subtract, multiply, divide
import pytest


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test the subtract function."""
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5


def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(1, 3) == pytest.approx(0.333, rel=1e-2)


def test_divide_by_zero():
    """Test that divide raises an exception on zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)