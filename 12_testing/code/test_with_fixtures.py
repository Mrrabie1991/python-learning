# test_with_fixtures.py — using fixtures

import pytest


# Fixture: A sample list shared among tests
@pytest.fixture
def sample_list():
    """Return a sample list for testing."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def empty_list():
    """Return an empty list."""
    return []


def test_list_length(sample_list):
    """Test length of sample list."""
    assert len(sample_list) == 5


def test_list_sum(sample_list):
    """Test sum of sample list."""
    assert sum(sample_list) == 15


def test_list_append(sample_list):
    """Test append to list."""
    sample_list.append(6)
    assert len(sample_list) == 6
    assert sample_list[-1] == 6


def test_empty_list(empty_list):
    """Test empty list behavior."""
    assert len(empty_list) == 0
    assert empty_list == []