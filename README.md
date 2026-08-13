# Automation Roadmap — Week 1

Week 1 of a 24-week roadmap to becoming an automation specialist. 
This week covers Python fundamentals needed before moving into n8n.

## Topics Covered

- Variables, types, and user input
- Conditionals and comparison operators
- Loops and the accumulator pattern
- Functions (parameters, return values)
- Reading and writing CSV files
- Working with JSON (dumps/loads/dump/load)
- Calling REST APIs with `requests`
- Error handling (status codes and try/except)
- Git basics (init, commit, push, .gitignore)

## Files

### Practice files
- `intro.py`, `variables.py`, `practice_day2.py` — basic syntax
- `def_practice*.py` — function exercises
- `loop_practice*.py` — loop and accumulator exercises
- `json_practice.py` — JSON conversion
- `api_practice.py` ... `api5_practice.py` — API calls and error handling

### Functional scripts
- `filter_CSV.py` — filters contacts by age
- `contacts_to_json.py` — converts CSV data to JSON
- `loop_practice6.py` — **Phase 1 final project**: validates contacts and separates valid from invalid records

## Phase 1 Final Project

Reads `contacts.CSV`, validates each record (name must not be empty, 
email must contain "@"), saves valid records to `valid_contacts.json`, 
and reports counts.

Run with:

    python loop_practice6.py

Output:

    valid: 3
    invalid: 2