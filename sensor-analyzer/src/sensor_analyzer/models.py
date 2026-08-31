# src/sensor_analyzer/models.py
"""Data models for sensor readings."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SensorReading:
    """A single sensor reading from a data file.

    Attributes:
        timestamp: Time when reading was taken.
        temperature: Temperature in Celsius. None if invalid.
        humidity: Humidity percentage. None if invalid.
        pressure: Atmospheric pressure in hPa. None if invalid.
    """

    timestamp: str
    temperature: Optional[float]
    humidity: Optional[float]
    pressure: Optional[float]

    @property
    def is_valid(self) -> bool:
        """Return True if all sensor values are valid."""
        return (
            self.temperature is not None
            and self.humidity is not None
            and self.pressure is not None
        )

    @property
    def missing_fields(self) -> list[str]:
        """Return list of field names that are missing or invalid."""
        missing = []

        if self.temperature is None:
            missing.append("temperature")
        if self.humidity is None:
            missing.append("humidity")
        if self.pressure is None:
            missing.append("pressure")

        return missing