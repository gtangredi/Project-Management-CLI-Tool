class Project:
    all = []

    def __init__(self, title, description, due_date, user_name):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_name = user_name
        Project.all.append(self)

    def tasks(self):
        from models.task import Task
        return [t for t in Task.all if t.project_title == self.title]

    def __str__(self):
        return f"{self.title} (due: {self.due_date}) - owner: {self.user_name}"
