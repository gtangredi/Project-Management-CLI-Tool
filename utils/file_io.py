import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/data.json")


def save_data(users, projects, tasks):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    data = {
        "users": [{"name": u.name, "email": u.email} for u in users],
        "projects": [
            {
                "title": p.title,
                "description": p.description,
                "due_date": p.due_date,
                "user_name": p.user_name,
            }
            for p in projects
        ],
        "tasks": [
            {
                "title": t.title,
                "project_title": t.project_title,
                "assigned_to": t.assigned_to,
                "status": t.status,
            }
            for t in tasks
        ],
    }
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except OSError as e:
        print(f"Error saving data: {e}")


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "projects": [], "tasks": []}
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read data file. Starting fresh.")
        return {"users": [], "projects": [], "tasks": []}
