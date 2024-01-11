import json
import os
from datetime import datetime

class ProjectManager:
    def __init__(self):
        self.projects = {}

    def save_data(self):
        with open('project_manager_data.json', 'w') as file:
            json.dump(self.projects, file)

    def load_data(self):
        if os.path.exists('project_manager_data.json'):
            with open('project_manager_data.json', 'r') as file:
                self.projects = json.load(file)

    def create_project(self, name):
        if name not in self.projects:
            self.projects[name] = {'tasks': []}
            print(f"Project '{name}' created successfully.")
            self.save_data()
        else:
            print(f"Project '{name}' already exists.")

    def add_task(self, project_name, task_name, due_date):
        if project_name in self.projects:
            task = {'name': task_name, 'due_date': due_date, 'completed': False}
            self.projects[project_name]['tasks'].append(task)
            print(f"Task '{task_name}' added to project '{project_name}'.")
            self.save_data()
        else:
            print(f"Project '{project_name}' does not exist.")

    def mark_task_completed(self, project_name, task_name):
        if project_name in self.projects:
            for task in self.projects[project_name]['tasks']:
                if task['name'] == task_name:
                    task['completed'] = True
                    print(f"Task '{task_name}' marked as completed.")
                    self.save_data()
                    return
            print(f"Task '{task_name}' not found in project '{project_name}'.")
        else:
            print(f"Project '{project_name}' does not exist.")

    def view_projects(self):
        print("Projects:")
        for project in self.projects:
            print(f"- {project}")
            print("  Tasks:")
            for task in self.projects[project]['tasks']:
                status = 'Completed' if task['completed'] else 'Not Completed'
                print(f"    - {task['name']} (Due: {task['due_date']}, Status: {status})")

if __name__ == "__main__":
    manager = ProjectManager()
    manager.load_data()

    while True:
        print("\nProject Manager Menu:")
        print("1. Create Project")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. View Projects")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            project_name = input("Enter project name: ")
            manager.create_project(project_name)
        elif choice == '2':
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(project_name, task_name, due_date)
        elif choice == '3':
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            manager.mark_task_completed(project_name, task_name)
        elif choice == '4':
            manager.view_projects()
        elif choice == '5':
            manager.save_data()
            print("Exiting the Project Manager. Data saved.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
