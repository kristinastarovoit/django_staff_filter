# Django Employee Filters

## Description

A small Django practice project created as part of the Developer Akademie for practicing QuerySet filters. One view loads employees with different filters and passes the results to a template via the context dictionary.


### Prerequisites
Python 3 and the packages listed in `requirements.txt` (installed with `pip freeze`), which includes Django.

## Quickstart
1. Set up the environment and database (use the Command Prompt (cmd)):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

2. Load the seed data:

```bash
python manage.py shell < populate.py
```

3. Start the development server:

```bash
python manage.py runserver
```

## Usage

Open the page rendered by `employee_overview`. It shows all employees, employees earning more than 3000, the number earning 5000 or more, the Sales employees with their average salary, and employees hired before 2022 who are not in HR.
