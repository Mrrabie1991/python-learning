# Sensor Data Analyzer

## Industrial Sensor Data Analysis Tool

A Python CLI tool for analyzing industrial sensor data from CSV files.

This project was built as the Phase 1 mini-project (Python Foundations) and combines the following concepts:

- Classes & OOP (`dataclass`, `@property`)
- File Handling (`with open()`, `csv.DictReader`)
- Exceptions (`try-except`)
- Type Hints (`Optional`, `Any`, `str | Path`)
- List & Dict Comprehension
- Package Structure (`src/`, `pyproject.toml`)
- Testing (`pytest`)

## Features

- Read sensor data from CSV files
- Detect invalid data (empty or non-numeric values)
- Calculate average, max, and min for each field
- Display text report in terminal
- Save JSON report

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate (Git Bash / Linux)
source venv/Scripts/activate

# Install project in development mode
pip install -e .
```

## Usage

```bash
# Display text report
python -m sensor_analyzer.cli data/sample_sensors.csv

# Save JSON report
python -m sensor_analyzer.cli data/sample_sensors.csv --json-output output/report.json
```

## Running Tests

```bash
pip install pytest
pytest
```

## Project Structure

```
sensor-analyzer/
├── src/
│   └── sensor_analyzer/
│       ├── __init__.py
│       ├── models.py          # SensorReading class
│       ├── reader.py          # CSV reading
│       ├── analyzer.py        # Data analysis
│       ├── reporter.py        # Reporting
│       └── cli.py             # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_reader.py
│   ├── test_analyzer.py
│   └── test_reporter.py
├── data/
│   └── sample_sensors.csv     # Sample data
├── output/                    # Generated reports
├── pyproject.toml
├── README.md
├── README_fa.md
├── .gitignore
└── requirements.txt

```

## Sample Output

```
=== Sensor Data Analysis Report ===

Summary:
  Total readings:   20
  Valid readings:   18
  Invalid readings: 2

Statistics:
  Temperature:
    Average: 27.89
    Max:     33.0
    Min:     22.5
    Count:   19
```

## Technical Notes

- Invalid CSV values are converted to `None`.
- `SensorReading.is_valid` checks if all fields are valid numbers.
- `missing_fields` reports which fields have invalid data.
- JSON report is saved with `ensure_ascii=False` to support non-ASCII characters.