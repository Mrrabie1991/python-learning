# src/sensor_analyzer/cli.py
"""Command-line interface for sensor analyzer."""

import argparse
import sys
from pathlib import Path

from .analyzer import analyze
from .reader import read_csv
from .reporter import format_report, save_json_report


def main() -> None:
    """Run the sensor analyzer CLI."""

    parser = argparse.ArgumentParser(
        description="Analyze industrial sensor data from CSV files"
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to CSV file with sensor data",
    )
    parser.add_argument(
        "--json-output",
        type=str,
        default=None,
        help="Save JSON report to specified path",
    )

    args = parser.parse_args()

    input_path = Path(args.input_file)

    try:
        readings = read_csv(input_path)
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        sys.exit(1)

    if not readings:
        print("Error: No data found in file.")
        sys.exit(1)

    analysis = analyze(readings)

    # Print formatted report
    print(format_report(analysis))

    # Save JSON report if requested
    if args.json_output:
        save_json_report(analysis, args.json_output)
        print(f"\nJSON report saved to: {args.json_output}")


if __name__ == "__main__":
    main()