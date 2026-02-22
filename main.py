import argparse
import sys

from tabulate import tabulate

from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import save_data, load_data


def load_all():
    data = load_data()
    for u in data["users"]:
        User(u["name"], u["email"])
    for p in data["projects"]:
        Project(p["title"], p["description"], p["due_date"], p["user_name"])
    for t in data["tasks"]:
        task = Task(t["title"], t["project_title"], t["assigned_to"])
        task.status = t["status"]


def save_all():
    save_data(User.all, Project.all, Task.all)


# ── Handlers ──────────────────────────────────────────────────────

def add_user(args):
    if any(u.name == args.name for u in User.all):
        print(f"Error: User '{args.name}' already exists.")
        sys.exit(1)
    User(args.name, args.email)
    save_all()
    print(f"User '{args.name}' created.")


def list_users(args):
    if not User.all:
        print("No users found.")
        return
    rows = [[u.name, u.email, len(u.projects())] for u in User.all]
    print(tabulate(rows, headers=["Name", "Email", "Projects"], tablefmt="simple"))


def add_project(args):
    if not any(u.name == args.user for u in User.all):
        print(f"Error: User '{args.user}' not found.")
        sys.exit(1)
    if any(p.title == args.title for p in Project.all):
        print(f"Error: Project '{args.title}' already exists.")
        sys.exit(1)
    Project(args.title, args.description, args.due_date, args.user)
    save_all()
    print(f"Project '{args.title}' created for user '{args.user}'.")


def list_projects(args):
    projects = Project.all
    if args.user:
        projects = [p for p in projects if p.user_name == args.user]
    if not projects:
        print("No projects found.")
        return
    rows = [[p.title, p.description, p.due_date, p.user_name] for p in projects]
    print(tabulate(rows, headers=["Title", "Description", "Due Date", "Owner"], tablefmt="simple"))


def add_task(args):
    if not any(p.title == args.project for p in Project.all):
        print(f"Error: Project '{args.project}' not found.")
        sys.exit(1)
    Task(args.title, args.project, args.assign)
    save_all()
    print(f"Task '{args.title}' added to project '{args.project}'.")


def list_tasks(args):
    tasks = [t for t in Task.all if t.project_title == args.project]
    if not tasks:
        print("No tasks found.")
        return
    rows = [[t.title, t.assigned_to or "none", t.status] for t in tasks]
    print(tabulate(rows, headers=["Title", "Assigned To", "Status"], tablefmt="simple"))


def complete_task(args):
    task = next(
        (t for t in Task.all if t.project_title == args.project and t.title == args.task),
        None,
    )
    if not task:
        print(f"Error: Task '{args.task}' not found in project '{args.project}'.")
        sys.exit(1)
    task.mark_complete()
    save_all()
    print(f"Task '{args.task}' marked as complete.")


# ── Parser ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    sub = parser.add_subparsers(dest="command")
    sub.required = True

    # add-user
    p = sub.add_parser("add-user")
    p.add_argument("--name", required=True)
    p.add_argument("--email", required=True)
    p.set_defaults(func=add_user)

    # list-users
    p = sub.add_parser("list-users")
    p.set_defaults(func=list_users)

    # add-project
    p = sub.add_parser("add-project")
    p.add_argument("--user", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--description", default="")
    p.add_argument("--due-date", dest="due_date", default="")
    p.set_defaults(func=add_project)

    # list-projects
    p = sub.add_parser("list-projects")
    p.add_argument("--user", default=None)
    p.set_defaults(func=list_projects)

    # add-task
    p = sub.add_parser("add-task")
    p.add_argument("--project", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--assign", default="")
    p.set_defaults(func=add_task)

    # list-tasks
    p = sub.add_parser("list-tasks")
    p.add_argument("--project", required=True)
    p.set_defaults(func=list_tasks)

    # complete-task
    p = sub.add_parser("complete-task")
    p.add_argument("--project", required=True)
    p.add_argument("--task", required=True)
    p.set_defaults(func=complete_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    load_all()
    main()
