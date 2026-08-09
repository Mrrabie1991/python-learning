# test_parametrize.py — one test, many inputs

from calculator import add , divide
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),        # positive + positive
    (-2, -3, -5),     # negative + negative
    (0, 5, 5),        # zero + positive
    (-1, 1, 0),       # negative + positive
    (100, 200, 300),  # large numbers
])
def test_add_parametrized(a, b, expected):
    """Test add with multiple inputs."""
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b", [
    (10, 0),
    (0, 0),
    (-5, 0),
])
def test_divide_by_zero_parametrized(a, b):
    """Test that divide raises on zero for multiple inputs."""
    with pytest.raises(ValueError):
        divide(a, b)