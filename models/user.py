class User:
    all = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.all.append(self)

    def projects(self):
        from models.project import Project
        return [p for p in Project.all if p.user_name == self.name]

    def __str__(self):
        return f"{self.name} ({self.email})"
