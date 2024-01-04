# Task Manager Application

This Task Manager application is a simple Python-based task management system that allows users to add tasks, mark them as completed, and view all tasks. It will be used as a code base for my DevOps course project @ FMI Sofia University. The project is a complete automated software delivery process with pipelines using some of the main topics covered in the course.

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

The project's workflow is like a series of connected steps that work together to make sure the software is good to go before it's shared with everyone. Each step relies on the previous one, creating a smooth flow.

GitHub Actions were employed to automate code style checks, linting processes, code security checks, database migrations checks, docker containerization and kubernetes deployment, ensuring consistent code quality and adherence to coding standards across the project.

Two GitHub Actions workflow files (.github/workflows/ci.yml and deployment.yml) were created to execute the prevoiusly mentioned pipeline. The first workflow is triggered on specific events, such as pushes and the deployment workflow is triggered on a successfull completion of the ci pipeline.

Jobs and Steps
The workflow consisted of the following jobs:

- editorconfig-checker
- flake8
- markdown-lint
- unittest
- sonar-cloud
- snyk
- gitleaks
- sql
- docker-build
- trivy
- docker-push

### 4. Continuous Integration

CI is a crucial aspect of the development process, enabling frequent code integration and automated testing to detect issues early in the development lifecycle. In my project, CI is employed to ensure code quality, verify changes, and maintain a consistent build process.

The CI workflow follows several essential steps:

It ensures code conformity with defined coding style and formatting using EditorConfig settings, checks the Python codebase for adherence to PEP 8 style guide and identifies syntax or formatting issues with Flake8, with Markdown-lint it verifies the structure and formatting of Markdown files to maintain consistency in documentation. Also executes unit tests defined in src/test_task_manager.py to validate the functionality of the Task Manager application.

Some security checks were added too: 

The pipeline performs a comprehensive code analysis to evaluate code quality, identify vulnerabilities, and provide insights into potential improvements via Sonar Cloud, scans dependencies to detect and report vulnerabilities in Python libraries used in the project with Snyk and then uses gitleaks to scan the repository for sensitive information leaks or accidental exposure of secrets in code and commit history.

SQL Database Migration Validation - validates the SQL database migrations using Flyway, ensuring smooth database schema updates.

Container Security Scan with Trivy - scans Docker images for potential security vulnerabilities before pushing to a container registry. Then pushes the Docker image to the specified Docker registry with the Docker push step.

Docker Build and Push - Builds the Docker image for the Task Manager application and pushes it to the specified Docker registry.

Benefits

- Continuous integration ensures that changes can be integrated smoothly, minimizing conflicts and enhancing code reliability.
- Immediate feedback from CI pipelines allows developers to rectify issues promptly, leading to faster iteration cycles.
- CI ensures that the application is deployed consistently across different environments, promoting reliability and reproducibility.

### 5. Continuous Deployment
