# Lab 5: Static Code Analysis - Inventory System

## Overview
This repository contains the solution for Lab 5: Static Code Analysis. The project demonstrates the use of static analysis tools (Pylint, Bandit, and Flake8) to improve Python code quality, security, and style.

## Repository Contents
- `inventory_system.py` - Original inventory system with issues
- `clean_inventory_system.py` - Fixed and improved version
- `pylint_report.txt` - Pylint analysis report (clean file)
- `bandit_report.txt` - Bandit security analysis report (clean file)
- `flake8_report.txt` - Flake8 style analysis report (clean file)
- `README.md` - This file

## Known Issues Table

| Issue Type | Tool | Line(s) | Severity | Description | Fix Approach |
|------------|------|---------|----------|-------------|--------------|
| Dangerous default value | Pylint | 8 | High | Mutable default argument `logs=[]` shared across function calls | Changed default to `None` and initialized inside function |
| Bare except | Pylint/Flake8 | 19 | High | Overly broad exception handler catches all errors | Replaced with specific exception types `(KeyError, TypeError)` |
| Security - eval() | Bandit | 59 | Medium | Use of dangerous `eval()` function allows arbitrary code execution | Removed dangerous eval() call entirely |
| Unused import | Pylint/Flake8 | 2 | Low | `logging` module imported but never used | Removed unused import |
| Missing module docstring | Pylint | 1 | Low | No module-level documentation | Added comprehensive module docstring |
| Missing function docstrings | Pylint | Multiple | Low | Functions lack documentation | Added docstrings to all functions |
| Non-snake_case naming | Pylint | Multiple | Low | Function names don't follow PEP 8 convention | Renamed to snake_case (e.g., `addItem` → `add_item`) |
| String formatting | Pylint | 12 | Low | Old-style string formatting with `%` | Replaced with f-strings for better readability |
| Missing encoding | Pylint | 26, 32 | Low | `open()` called without explicit encoding | Added `encoding="utf-8"` parameter |
| Context manager | Pylint | 26, 32 | Low | Files opened without using `with` statement | Wrapped file operations in `with` context manager |
| PEP 8 blank lines | Flake8 | Multiple | Low | Missing blank lines between functions | Added 2 blank lines between top-level functions |
| Missing final newline | Pylint/Flake8 | 61 | Low | File doesn't end with newline | Added newline at end of file |
| Input validation | Custom | 8, 50 | Medium | Functions accept invalid types without validation | Added type checking and validation |
| Error handling | Custom | 14-20 | Medium | Poor error messages and silent failures | Added informative error messages |

**Total Issues Fixed: 14**

## Improvements Made

### 1. Security Improvements
- Removed dangerous `eval()` function call
- Added proper exception handling with specific exception types
- Added input validation to prevent type errors

### 2. Code Quality Improvements
- Added comprehensive docstrings to all functions
- Renamed functions to follow snake_case convention
- Replaced old-style string formatting with f-strings
- Removed unused imports
- Added type validation for function parameters

### 3. Style Improvements (PEP 8 Compliance)
- Added proper spacing (2 blank lines between functions)
- Added final newline at end of file
- Used context managers (`with` statement) for file operations
- Specified encoding for file operations
- Added module docstring

### 4. Robustness Improvements
- Fixed mutable default argument bug
- Added error handling for file not found scenarios
- Added informative error messages
- Used `.get()` method for safer dictionary access
- Added `if __name__ == "__main__":` guard

## Analysis Results

### Pylint Score
- **Original**: 4.60/10
- **Clean Version**: 10.00/10

### Bandit Security Issues
- **Original**: 2 issues (1 Medium, 1 Low)
- **Clean Version**: 0 issues

### Flake8 Style Issues
- **Original**: 12 issues
- **Clean Version**: 0 issues

## Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest to fix:**
- Style issues like missing blank lines, final newlines, and naming conventions were straightforward to fix as they only required formatting changes
- Removing unused imports was a simple deletion
- Converting string formatting from `%` to f-strings was a simple find-and-replace operation

**Hardest to fix:**
- The mutable default argument bug required understanding how Python handles default arguments and their persistence across function calls
- Proper exception handling required understanding what specific exceptions could occur and handling them appropriately
- Input validation required thinking through all possible edge cases and invalid inputs

### 2. Did the static analysis tools report any false positives? If so, describe one example.

The `global-statement` warning from Pylint (line 27) could be considered somewhat of a false positive in this context. While using global variables is generally discouraged, for a simple inventory system demonstration, it's an acceptable design choice. However, I kept the warning suppressed with a comment as it's intentional in this case.

All other warnings were legitimate issues that improved code quality when addressed.

### 3. How would you integrate static analysis tools into your actual software development workflow?

**Pre-commit hooks:**
- Configure Git hooks to run Flake8 and Pylint before each commit
- Prevent commits if critical issues are found

**CI/CD Pipeline:**
- Add static analysis as a required step in GitHub Actions/Jenkins
- Run Pylint, Bandit, and Flake8 on every pull request
- Set minimum quality thresholds (e.g., Pylint score > 8.0)
- Block merges if security issues are detected by Bandit

**IDE Integration:**
- Install Pylint, Flake8 extensions in VS Code
- Configure real-time linting to catch issues while coding
- Set up auto-formatting with Black or autopep8

**Regular Code Reviews:**
- Review static analysis reports weekly
- Address technical debt incrementally
- Track code quality metrics over time

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

**Readability:**
- F-strings make output formatting much clearer and easier to understand
- Descriptive function names (snake_case) are more Pythonic and readable
- Docstrings provide immediate context about what each function does
- Proper spacing makes the code structure clearer

**Robustness:**
- Input validation prevents crashes from invalid data types
- Specific exception handling prevents silent failures
- Context managers ensure files are properly closed even if errors occur
- Fixed mutable default argument prevents subtle bugs from shared state

**Maintainability:**
- Comprehensive documentation makes future modifications easier
- Consistent style reduces cognitive load when reading code
- Proper error messages help with debugging

**Security:**
- Removal of `eval()` eliminates a major security vulnerability
- Better exception handling prevents information leakage through error messages

The code went from a 4.60/10 to a perfect 10/10 on Pylint, with zero security issues and complete PEP 8 compliance. This demonstrates the significant value that static analysis tools provide in creating professional, production-ready code.

## How to Run

1. Install dependencies:
```bash
pip install pylint bandit flake8
```

2. Run the clean inventory system:
```bash
python clean_inventory_system.py
```

3. Run static analysis:
```bash
pylint clean_inventory_system.py
bandit clean_inventory_system.py
flake8 clean_inventory_system.py
```

## Author
Suchith (PES1UG23AM321)