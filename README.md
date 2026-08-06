# # Automation Roadmap — Week 1

This is Week 1 of a 24-week roadmap to becoming an automation specialist. This week focuses on the Python fundamentals needed before moving into automation tools like n8n.

## Files

### Practice files
No specific pattern — just for learning core Python concepts.
- `Hello.py`
- `intro.py`
- `practice_day2.py`
- `variables.py` — introduces what variables mean in Python

### Functional files
- `read_CSV.py` — reads and displays the contents of a CSV file
- `filter_CSV.py` — filters and organizes data from `contacts.CSV` based on the logic written in the code
- `contacts.CSV` — sample input data (names, emails, messages)
- `filtered_contacts.csv` — sample output after filtering

## How to run

1. Navigate to this folder in PowerShell:

cd path\to\week01


2. Activate the virtual environment:

.\venv\Scripts\Activate.ps1


3. Run the CSV filter script:

python filter_CSV.py


## Workflow

`read_CSV.py` reads the raw data from `contacts.CSV`. `filter_CSV.py` then applies filtering logic and produces `filtered_contacts.csv` as the cleaned/filtered output.