# src/sensor_analyzer/analyzer.py
"""Analyze sensor data."""

from typing import Any

from .models import SensorReading


def _analyze_field(readings: list[SensorReading], field: str) -> dict[str, Any]:
    """Calculate average, max, and min for a sensor field."""
    values = [
        getattr(r, field)
        for r in readings
        if getattr(r, field) is not None
    ]

    if not values:
        return {
            "average": None,
            "max": None,
            "min": None,
            "count": 0,
        }

    return {
        "average": round(sum(values) / len(values), 2),
        "max": max(values),
        "min": min(values),
        "count": len(values),
    }


def analyze(readings: list[SensorReading]) -> dict[str, Any]:
    """Analyze a list of sensor readings.

    Args:
        readings: List of SensorReading objects.

    Returns:
        Dictionary with summary and per-field statistics.
    """

    valid_readings = [r for r in readings if r.is_valid]
    invalid_readings = [r for r in readings if not r.is_valid]

    summary = {
        "total_readings": len(readings),
        "valid_readings": len(valid_readings),
        "invalid_readings": len(invalid_readings),
    }

    # Collect missing fields info
    missing_fields: dict[str, int] = {}

    for reading in invalid_readings:
        for field in reading.missing_fields:
            missing_fields[field] = missing_fields.get(field, 0) + 1

    return {
        "summary": summary,
        "temperature": _analyze_field(readings, "temperature"),
        "humidity": _analyze_field(readings, "humidity"),
        "pressure": _analyze_field(readings, "pressure"),
        "missing_fields": missing_fields,
    }