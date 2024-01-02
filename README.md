# Task Manager Application

This Task Manager application is a simple Python-based task management system that allows users to add tasks, mark them as completed, and view all tasks. It will be used as a code base for my DevOps course project @ FMI Sofia University. The project is a complete automated software delivery process with pipelines using some of the main topics covered in the course.

## Features

- Add new tasks to the task list.
- Mark tasks as completed.
- View the list of all tasks.

## CI/CD

The following topics are addressed in the project:

### 1. Source control and collaboration

This project's development process heavily relied on efficient source control management using Git and collaboration tracking via GitHub Issues. These tools were instrumental in organizing tasks, managing versions, facilitating collaboration, and ensuring a streamlined development workflow.

Git, a distributed version control system, was the backbone of this project's source control. GitHub Issues served as the primary project management tool. It helps for:

- Create and assign tasks, enhancements, bugs, or documentation improvements.
- Organize issues using labels, milestones, and assignees for better prioritization and visibility.

Workflow

The typical workflow for a new feature or task involved:

- A new GitHub Issue creation for a specific task or feature.
- A new branch from the main branch with a descriptive name related to the issue.
- Work was carried out in the feature branch, committing changes regularly.
- Once completed, a Pull Request (PR) was opened to merge changes into the main branch.

### 2. Branching strategy

The Gitflow branching model was followed, which consisted of the following branches:

- Main branch (in this particular case used as main and develop branch since there was only one developer working on the project):  Production-ready code and ongoing development
- Feature branches: Created for each new feature or task, merged into the main branch upon completion.

### 3. Building pipelines

GitHub Actions were employed to automate code style checks and linting processes, ensuring consistent code quality and adherence to coding standards across the project.

A GitHub Actions workflow file (.github/workflows/ci.yml) was created to execute code style checks and linting. This workflow was triggered on specific events, such as pushes or pull requests.

Jobs and Steps
The workflow consisted of the following jobs:

- editorconfig-checker: a step utilizing the editorconfig-checker action to validate consistency with .editorconfig settings
- flake8: utilization of the flake8 action for Python linting, ensuring adherence to PEP 8 coding standards
- markdown-lint: a step using the markdown-lint action to verify adherence to markdown formatting standards in markdown files
