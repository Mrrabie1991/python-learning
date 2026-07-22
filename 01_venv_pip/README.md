# 01 - Virtual Environment & pip

## What I Learned

A Virtual Environment is an isolated environment for each Python project. It prevents dependencies from different projects from conflicting with each other.

## Comparison with C++

In C++, I used to manage dependencies manually with CMake and a Dependencies folder.
In Python, venv automates this by creating a virtual copy of Python itself.

## Commands I Learned

### Create
```bash
python -m venv venv
```

### Activate
```bash
# Linux / macOS / Git Bash on Windows
source venv/bin/activate
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Windows Command Prompt
venv\Scripts\activate.bat
```

### Deactivate
```bash
deactivate
```

### List Installed Packages
```bash
pip list
```

## Notes
- The `venv/` folder should NEVER be committed to Git.
- Instead, we commit a `requirements.txt` file (to be covered later).

## Saving & Restoring Dependencies

### Save (freeze)
```bash
pip freeze > requirements.txt
```

### Restore
```bash
pip install -r requirements.txt
```

### Example
After installing `requests` and running freeze, requirements.txt includes requests and its dependencies (urllib3, certifi, ...). This file replaces committing the venv/ folder.