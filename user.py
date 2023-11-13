# user.py

from project import Project

class User:
	def __init__(self, username):
		self.username = username
		self.projects = []

	def create_projects(self, project_name):
		project = Project(project_name)
		self.projects.append(project)

	def __str__(self):
		return f"Username: {self.username}\nProjects: {', '.join(project.name for project in self.projects)}"
