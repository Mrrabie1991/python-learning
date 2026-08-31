# tests/test_reader.py
"""Tests for reader module."""

import pytest

from sensor_analyzer.reader import read_csv, _parse_float


def test_parse_float_valid():
    """Valid numbers should convert to float."""
    assert _parse_float("25.5") == 25.5
    assert _parse_float("0") == 0.0
    assert _parse_float("-10.3") == -10.3


def test_parse_float_invalid():
    """Invalid values should return None."""
    assert _parse_float("") is None
    assert _parse_float("invalid") is None
    assert _parse_float(None) is None


def test_read_csv(tmp_path):
    """Read CSV file and return SensorReading list."""
    csv_content = (
        "timestamp,temperature,humidity,pressure\n"
        "2026-01-01 08:00:00,22.5,45.2,1013.2\n"
        "2026-01-01 08:05:00,23.1,46.8,1012.8\n"
    )

    csv_file = tmp_path / "test_sensors.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    readings = read_csv(csv_file)

    assert len(readings) == 2
    assert readings[0].temperature == 22.5
    assert readings[1].humidity == 46.8


def test_read_csv_with_invalid_values(tmp_path):
    """Invalid numeric values should become None."""
    csv_content = (
        "timestamp,temperature,humidity,pressure\n"
        "2026-01-01 08:00:00,,45.2,1013.2\n"
        "2026-01-01 08:05:00,23.1,invalid,1012.8\n"
    )

    csv_file = tmp_path / "test_invalid.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    readings = read_csv(csv_file)

    assert readings[0].temperature is None
    assert readings[1].humidity is None


def test_read_csv_missing_file():
    """Missing file should raise FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_csv("nonexistent_file.csv")