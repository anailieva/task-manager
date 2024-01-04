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

### 5. Continuous Delivery

Continuous Delivery in this project automates the steps needed to get any changes we make to the software ready for deployment quickly and reliably. This ensures that our software is always up-to-date, well-tested, and ready for use.

However, the actual deployment to Kubernetes occurs in a separate workflow that handles the deployment of the thoroughly scanned and checked Docker images.

Deployment Workflow

Concentrates on deploying the pre-scanned and quality-assured Docker images to the Kubernetes environment. This workflow occurs after the Continuous Delivery process to ensure a clear separation of concerns. The division separates the responsibilities clearly, ensuring a seamless transition from preparing the software to deploying it. It also ensures that only thoroughly checked and verified images are pushed into the production environment, minimizing risks.

### 6. Security

#### SonarCloud

SonarCloud performs an in-depth static analysis of the codebase, identifying potential vulnerabilities, code smells, and bugs. For instance - it flags security-sensitive code patterns such as hardcoded credentials or potential SQL injection points in our codebase. Integrated into our CI process, SonarCloud continuously monitors our code changes - upon every pull request, SonarCloud automatically reviews new code additions, ensuring that introduced code maintains security and quality standards.

Language Support
It supports multiple programming languages including Java, JavaScript, TypeScript, Python, C#, C/C++, PHP, Swift, and more.

SonarCloud allows you to define quality criteria for your project, and the Quality Gate ensures that your code meets these criteria before it can be merged or released.

How SonarCloud Works

SonarCloud analyzes your code using static code analysis techniques. It identifies and flags issues like bugs, vulnerabilities, code smells, and more. It provides comprehensive reports and dashboards displaying the detected issues, their severity, and recommendations for improvement. SonarCloud checks if your code meets predefined quality criteria. If not, it prevents the merge or release of poor-quality code.

Benefits of Using SonarCloud

Helps improve code quality by identifying and resolving issues early in the development cycle. Detects security vulnerabilities, providing guidance to mitigate risks. Helps in maintaining code standards, readability, and maintainability. Integrates seamlessly with CI/CD pipelines and other development tools, making it easy to incorporate code analysis into your workflows.

#### Snyk

Snyk specializes in scanning project dependencies for vulnerabilities. It identifies known vulnerabilities in third-party libraries. For instance, it may detect a vulnerable version of a package used in our Python dependencies. Snyk offers remediation advice for addressing detected vulnerabilities - it suggests updating a vulnerable package to a patched version or provides alternative dependency options to mitigate the security risk.

How Snyk Works

Snyk analyzes your project dependencies, checking against its extensive database of known vulnerabilities. It identifies vulnerabilities in dependencies and container images. Snyk provides guidance on how to remediate vulnerabilities, suggesting specific updates or patches to fix the issues. Offers continuous monitoring to stay updated on newly discovered vulnerabilities affecting your dependencies. To integrate Snyk with GitHub Actions, you can use the Snyk GitHub Action within your workflows. The action requires configuration, including Snyk authentication token, project details, and other optional parameters.

#### Trivy

Trivy scans Docker container images for OS and application-level vulnerabilities. It detects critical vulnerabilities within the base operating system of our Docker images or flags insecure configurations within the application setup within the container. Trivy focuses on identifying high-severity vulnerabilities that pose significant risks - it identifies a critical vulnerability within a specific software library or an unpatched component, prompting immediate remediation actions.

#### Benefits of Security Checks

- Early Threat Identification - By leveraging SonarCloud, Snyk, and Trivy, we can identify potential security threats early in the development lifecycle, allowing for timely resolution.
- Enhanced Security Posture - These tools aid in maintaining a robust security posture by addressing vulnerabilities promptly and continuously.

### 7. Docker

The application is containerized using Docker, ensuring consistency and reproducibility across different development environments. Docker containers encapsulate the application and its dependencies, allowing developers to work in isolated environments without interference from system-specific configurations. Within our CI pipeline, Docker is used to build our application, ensuring consistency between the development environment and the build environment. We run automated tests within Docker containers to validate the application's functionality in a controlled and reproducible environment. Docker enables versioning and tagging of container images, facilitating easy rollback or updates in case of issues or new releases. Docker images are deployed and managed within Kubernetes clusters, ensuring scalability, resilience, and efficient resource utilization. Kubernetes leverages Docker containers to orchestrate application deployment, scaling, and management across clusters of nodes.

### 8. Kubernetes

Kubernetes serves as a cornerstone for orchestrating and managing containerized applications. It streamlines deployment, scaling, and management of containerized workloads. Kubernetes orchestrates the deployment of Docker container images across clusters of nodes. It efficiently allocates computing resources, ensuring optimal performance and utilization across the deployment. Kubernetes facilitates horizontal scaling, allowing our application to scale by adding or removing instances based on demand. Through replication and automated failover, Kubernetes ensures high availability by distributing workloads across multiple nodes. Kubernetes abstracts services, enabling seamless communication between different parts of our application through defined service endpoints. It provides built-in load balancing capabilities to evenly distribute traffic across multiple instances of an application. Kubernetes allows for continuous deployment by automating the rollout of new versions or updates to our application.

Deployment YAML
Defines how the application should be deployed within the Kubernetes cluster. Specifies the deployment configuration, including the Docker image, number of replicas, and other deployment-related settings.

Service YAML
Defines how external services or users access the application. Specifies the service type (ClusterIP, NodePort, LoadBalancer), port configuration, and selectors to route traffic to the appropriate pods.
