# tests/test_analyzer.py
"""Tests for analyzer module."""

from sensor_analyzer.analyzer import analyze
from sensor_analyzer.models import SensorReading


def _make_reading(temp, humidity, pressure, timestamp="2026-01-01 08:00:00"):
    """Helper to create SensorReading."""
    return SensorReading(
        timestamp=timestamp,
        temperature=temp,
        humidity=humidity,
        pressure=pressure,
    )


def test_analyze_all_valid():
    """All valid readings should be counted."""
    readings = [
        _make_reading(22.0, 45.0, 1013.0),
        _make_reading(24.0, 47.0, 1015.0),
        _make_reading(26.0, 49.0, 1017.0),
    ]

    result = analyze(readings)

    assert result["summary"]["total_readings"] == 3
    assert result["summary"]["valid_readings"] == 3
    assert result["summary"]["invalid_readings"] == 0


def test_analyze_with_invalid():
    """Invalid readings should be counted separately."""
    readings = [
        _make_reading(22.0, 45.0, 1013.0),
        _make_reading(None, 47.0, 1015.0),
        _make_reading(26.0, None, 1017.0),
    ]

    result = analyze(readings)

    assert result["summary"]["total_readings"] == 3
    assert result["summary"]["valid_readings"] == 1
    assert result["summary"]["invalid_readings"] == 2


def test_analyze_temperature_stats():
    """Temperature statistics should be correct."""
    readings = [
        _make_reading(20.0, 45.0, 1013.0),
        _make_reading(24.0, 47.0, 1015.0),
        _make_reading(28.0, 49.0, 1017.0),
    ]

    result = analyze(readings)

    assert result["temperature"]["average"] == 24.0
    assert result["temperature"]["max"] == 28.0
    assert result["temperature"]["min"] == 20.0
    assert result["temperature"]["count"] == 3


def test_analyze_missing_fields_count():
    """Missing fields should be tracked."""
    readings = [
        _make_reading(None, 45.0, 1013.0),
        _make_reading(24.0, None, None),
    ]

    result = analyze(readings)

    assert result["missing_fields"]["temperature"] == 1
    assert result["missing_fields"]["humidity"] == 1
    assert result["missing_fields"]["pressure"] == 1