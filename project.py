# project.py

from task import Task

class Project:
	def __init__(self, name):
		self.name = name
		self.tasks = []

	def add_task(self, task):
		self.tasks.append(task)

	def remove_task(self, task):
		self.tasks.remove(task)

	def display_tasks(self):
		if not self.tasks:
			print(f"No tasks in the project '{self.name}'.")
		else:
			print(f"Tasks in the same project '{self.name}':")
			for task in self.tasks:
				print(task)

	def __str__(self):
		return f"Project Name: {self.name}\nNumber of Tasks: {len(self.tasks)}"
