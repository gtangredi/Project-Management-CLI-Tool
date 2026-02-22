# Project Management CLI Tool

A command-line tool to manage users, projects, and tasks. Data is saved to a local JSON file.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Users
python main.py add-user --name "Alex" --email "alex@gmail.com"
python main.py list-users

# Projects
python main.py add-project --user "Alex" --title "My Project" --description "Some work" --due-date "2025-12-31"
python main.py list-projects
python main.py list-projects --user "Alex"

# Tasks
python main.py add-task --project "My Project" --title "Do something" --assign "Alex"
python main.py list-tasks --project "My Project"
python main.py complete-task --project "My Project" --task "Do something"
```

## Running Tests

```bash
pytest tests/ -v
```

## Project Structure

```
pm/
├── main.py          # CLI entry point
├── models/
│   ├── user.py      # User class
│   ├── project.py   # Project class
│   └── task.py      # Task class
├── utils/
│   └── file_io.py   # Save/load JSON data
├── data/
│   └── data.json    # Auto-generated data file
├── tests/
│   └── test_models.py
├── requirements.txt
└── README.md
```

## External Package

Uses `tabulate` for formatted table output (listed in requirements.txt).

## Known Issues

- Project titles must be unique across all users.
