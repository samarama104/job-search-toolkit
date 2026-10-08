# job-search-toolkit
Small Python tools for organizing and analyzing a job search.

# Job Search Toolkit

A Python command-line tool that reads a CSV of job applications
and prints a summary of application statuses.

## Features

- Counts total applications.
- Counts Applied, Interview, and Rejected statuses.
- Handles capitalization and surrounding spaces in status labels.

## Requirements

Python 3. No additional packages are needed.

## How to run

1. Download or clone this repository.
2. Open a terminal in the repository folder.
3. Run:

```bash
python3 application_summary.py
```

## Input

The included applications.csv contains fictional sample data:

```csv
company,role,status,date_applied
Example Labs,Junior Developer,Applied,2026-10-01
```

## Example output

With the original five sample applications:

```text
Total applications: 5
Applied: 3
Interview: 1
Rejected: 1
```

## What I practiced

- Reading CSV files with Python's csv module.
- Accessing dictionary values.
- Using loops, counters, and conditional statements.
- Checking program output against sample data.

## Limitations

The script expects applications.csv in the current folder.
It counts predefined statuses and does not validate dates.