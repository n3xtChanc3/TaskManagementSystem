# task.py

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Not Completed"

    def mark_as_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"Title: {self.title} Description: {self.description} Due Date: {self.due_date} Status: {self.status}"
