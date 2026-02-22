import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user import User
from models.project import Project
from models.task import Task


@pytest.fixture(autouse=True)
def reset():
    User.all.clear()
    Project.all.clear()
    Task.all.clear()


# User tests
def test_create_user():
    u = User("Alex", "alex@gmail.com")
    assert u.name == "Alex"
    assert u.email == "alex@gmail.com"
    assert u in User.all

def test_user_projects():
    u = User("Alex", "alex@gmail.com")
    Project("P1", "", "", "Alex")
    assert len(u.projects()) == 1

def test_user_str():
    u = User("Alex", "alex@gmail.com")
    assert "Alex" in str(u)


# Project tests
def test_create_project():
    User("Alex", "alex@gmail.com")
    p = Project("My Project", "desc", "2025-12-31", "Alex")
    assert p.title == "My Project"
    assert p in Project.all

def test_project_tasks():
    p = Project("P1", "", "", "Alex")
    Task("T1", "P1")
    assert len(p.tasks()) == 1

def test_project_str():
    p = Project("P1", "", "2025-12-31", "Alex")
    assert "P1" in str(p)


# Task tests
def test_create_task():
    t = Task("Do something", "P1", "Alex")
    assert t.title == "Do something"
    assert t.status == "pending"
    assert t in Task.all

def test_mark_complete():
    t = Task("Do something", "P1")
    t.mark_complete()
    assert t.status == "complete"

def test_task_str():
    t = Task("Do something", "P1")
    assert "Do something" in str(t)
