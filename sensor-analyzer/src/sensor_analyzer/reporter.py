# src/sensor_analyzer/reporter.py
"""Generate reports from analysis results."""

import json
from pathlib import Path
from typing import Any


def format_report(analysis: dict[str, Any]) -> str:
    """Format analysis results as readable text.

    Args:
        analysis: Analysis result from analyzer.analyze().

    Returns:
        Formatted text string.
    """

    summary = analysis["summary"]
    lines: list[str] = []

    lines.append("=== Sensor Data Analysis Report ===")
    lines.append("")
    lines.append("Summary:")
    lines.append(f"  Total readings:   {summary['total_readings']}")
    lines.append(f"  Valid readings:   {summary['valid_readings']}")
    lines.append(f"  Invalid readings: {summary['invalid_readings']}")
    lines.append("")

    lines.append("Statistics:")
    for field in ["temperature", "humidity", "pressure"]:
        stats = analysis[field]
        lines.append(f"  {field.capitalize()}:")
        lines.append(f"    Average: {stats['average']}")
        lines.append(f"    Max:     {stats['max']}")
        lines.append(f"    Min:     {stats['min']}")
        lines.append(f"    Count:   {stats['count']}")
        lines.append("")

    if analysis["missing_fields"]:
        lines.append("Missing/Invalid Fields:")
        for field, count in analysis["missing_fields"].items():
            lines.append(f"  {field}: {count} occurrences")
        lines.append("")

    return "\n".join(lines)


def save_json_report(analysis: dict[str, Any], output_path: str | Path) -> None:
    """Save analysis results as JSON file.

    Args:
        analysis: Analysis result from analyzer.analyze().
        output_path: Path to save JSON report.
    """

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(analysis, file, indent=2, ensure_ascii=False)