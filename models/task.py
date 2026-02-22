class Task:
    all = []

    def __init__(self, title, project_title, assigned_to=""):
        self.title = title
        self.project_title = project_title
        self.assigned_to = assigned_to
        self.status = "pending"
        Task.all.append(self)

    def mark_complete(self):
        self.status = "complete"

    def __str__(self):
        return f"[{self.status}] {self.title} (assigned: {self.assigned_to or 'none'})"
