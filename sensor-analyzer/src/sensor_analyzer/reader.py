# src/sensor_analyzer/reader.py
"""Read sensor data from CSV files."""

import csv
from pathlib import Path
from typing import Optional

from .models import SensorReading


def _parse_float(value: str) -> Optional[float]:
    """Convert string to float. Return None if conversion fails."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def read_csv(filepath: str | Path) -> list[SensorReading]:
    """Read sensor readings from a CSV file.

    Expected CSV columns:
        timestamp, temperature, humidity, pressure

    Invalid numeric values (empty or non-numeric) become None.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of SensorReading objects.

    Raises:
        FileNotFoundError: If the file does not exist.
    """

    path = Path(filepath)
    readings: list[SensorReading] = []

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            reading = SensorReading(
                timestamp=row["timestamp"],
                temperature=_parse_float(row["temperature"]),
                humidity=_parse_float(row["humidity"]),
                pressure=_parse_float(row["pressure"]),
            )
            readings.append(reading)

    return readings