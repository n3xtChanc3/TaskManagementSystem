# main.py

from task import Task
from user import User

# Create a task
task1 = Task("Complete Assignment", "Finish the programming assignment", "2023-11-30")

# Create a user
user1 = User("Zdravko")

# Create a project for the user
user1.create_projects("Personal Tasks")

# Add the task to the project
user1.projects[0].add_task(task1)

# Display user information
print(user1)

# Display tasks in the project
user1.projects[0].display_tasks()
