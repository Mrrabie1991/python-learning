# tests/test_reporter.py
"""Tests for reporter module."""

import json

from sensor_analyzer.reporter import format_report, save_json_report


def test_format_report_contains_summary():
    """Report should contain summary info."""
    analysis = {
        "summary": {
            "total_readings": 10,
            "valid_readings": 8,
            "invalid_readings": 2,
        },
        "temperature": {
            "average": 25.0,
            "max": 30.0,
            "min": 20.0,
            "count": 10,
        },
        "humidity": {
            "average": 50.0,
            "max": 60.0,
            "min": 40.0,
            "count": 10,
        },
        "pressure": {
            "average": 1013.0,
            "max": 1015.0,
            "min": 1011.0,
            "count": 10,
        },
        "missing_fields": {"temperature": 2},
    }

    report = format_report(analysis)

    assert "Sensor Data Analysis Report" in report
    assert "Total readings:   10" in report
    assert "Valid readings:   8" in report
    assert "Invalid readings: 2" in report


def test_save_json_report(tmp_path):
    """JSON report should be saved with correct content."""
    analysis = {
        "summary": {
            "total_readings": 5,
            "valid_readings": 5,
            "invalid_readings": 0,
        },
        "temperature": {
            "average": 25.0,
            "max": 30.0,
            "min": 20.0,
            "count": 5,
        },
        "humidity": {
            "average": 50.0,
            "max": 60.0,
            "min": 40.0,
            "count": 5,
        },
        "pressure": {
            "average": 1013.0,
            "max": 1015.0,
            "min": 1011.0,
            "count": 5,
        },
        "missing_fields": {},
    }

    output_path = tmp_path / "report.json"
    save_json_report(analysis, output_path)

    with open(output_path, "r", encoding="utf-8") as file:
        loaded = json.load(file)

    assert loaded["summary"]["total_readings"] == 5
    assert loaded["temperature"]["average"] == 25.0