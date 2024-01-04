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

Security in this project is a fundamental aspect ensuring the robustness and reliability of the application. The development process integrates several security checks and measures to mitigate potential vulnerabilities and maintain a secure codebase. The embedded in the CI/CD pipeline checks facilitate early detection and resolution of security vulnerabilities, fostering a more secure software development lifecycle.

#### SonarCloud

SonarCloud is a cloud-based code analysis service designed to detect coding issues in 26 different programming languages. SonarCloud performs an in-depth static analysis of the codebase, identifying potential vulnerabilities, code smells, and bugs. For instance - it flags security-sensitive code patterns such as hardcoded credentials or potential SQL injection points in our codebase. Integrated into our CI process, SonarCloud continuously monitors our code changes - upon every pull request, SonarCloud automatically reviews new code additions, ensuring that introduced code maintains security and quality standards. As a core element of the Sonar solution, SonarCloud completes the analysis loop to help you deliver clean code that meets high-quality standards.

Code Analysis Process:

- Developers integrate SonarCloud into their development process by connecting it to their version control system (e.g., GitHub, GitLab, Bitbucket).
- Whenever code changes are made, developers can configure triggers to automatically initiate code analysis on SonarCloud. It can also be manually triggered.
- SonarCloud performs static code analysis using a wide range of built-in and customizable rules. These rules cover various programming languages (e.g., Java, JavaScript, Python, C#, etc.) and aspects such as code complexity, bugs, security vulnerabilities, coding standards, and best practices.

Detection of Issues

- SonarCloud identifies code smells that might indicate design issues or areas of code that could be improved for better readability, maintainability, or performance.
- It detects potential bugs or errors in the code that could cause runtime issues or unexpected behavior.
- Security vulnerabilities, such as potential weaknesses or loopholes, are flagged to ensure that sensitive data is protected.
- It identifies redundant or duplicated code sections that could lead to maintainability issues.

Reporting and Visualization

- SonarCloud provides a dashboard displaying an overview of code quality metrics, issues found, and their severity.
- Detailed reports are generated, highlighting specific issues with explanations and recommendations on how to resolve them.
- Developers can track code quality trends over time and view historical data to understand improvements or regressions.

Integration and Feedback Loop

- Developers can integrate SonarLint, a companion IDE plugin, which provides real-time feedback during coding, helping to catch issues early in the development process.
- SonarCloud can be configured to automatically analyze code changes made in pull requests, providing feedback before merging the code into the main branch.
- Developers receive actionable feedback directly within their development environment, enabling them to make necessary improvements promptly.

Customization and Extensibility

- Developers can customize or create their own rules based on their project's specific needs.
- SonarCloud seamlessly integrates into Continuous Integration/Continuous Deployment (CI/CD) pipelines, ensuring that code analysis is an integral part of the development lifecycle.

#### Snyk

Snyk specializes in scanning project dependencies for vulnerabilities. It identifies known vulnerabilities in third-party libraries. For instance, it may detect a vulnerable version of a package used in our Python dependencies. Snyk offers remediation advice for addressing detected vulnerabilities - it suggests updating a vulnerable package to a patched version or provides alternative dependency options to mitigate the security risk.

Vulnerability Detection

- Snyk starts by scanning and analyzing dependencies within the project. It identifies open source libraries and components used in the codebase.
- Snyk maintains a comprehensive and constantly updated database of known vulnerabilities and security issues associated with various libraries and packages across different programming languages and ecosystems.

Continuous Monitoring

- Snyk continuously monitors the libraries and dependencies used in the project, alerting to newly discovered vulnerabilities that might impact the code.
- It provides real-time alerts and notifications about vulnerabilities affecting the codebase.

Integration into Development Workflow

- Snyk integrates with popular Integrated Development Environments (IDEs) like Visual Studio Code, IntelliJ IDEA, and others, offering developers real-time feedback on vulnerabilities as they write code.
- Snyk seamlessly integrates with version control systems (e.g., GitHub, GitLab, Bitbucket) to scan projects for vulnerabilities as part of the development workflow.
- Snyk can be integrated into Continuous Integration/Continuous Deployment (CI/CD) pipelines, allowing automated scanning and analysis of code changes at various stages of the development process.

Remediation and Fixing Vulnerabilities

- When vulnerabilities are detected, Snyk provides actionable insights and guidance on how to remediate the issues, including suggested patches, upgrades, or alternative libraries.
- In some cases, Snyk can automatically generate pull requests (PRs) or suggest fixes to address vulnerabilities, streamlining the process of resolving security issues.

Container Security

- Snyk extends its capabilities to scan container images, identifying vulnerabilities in Docker images or Kubernetes deployments.
- It integrates with container registries to scan images stored in repositories, ensuring that containerized applications are free from known vulnerabilities.

Policy Enforcement and Compliance

- Snyk allows organizations to define and enforce security policies based on their specific requirements and compliance standards.
- It provides reports and insights into compliance status, helping teams ensure adherence to security standards and regulations.

Education and Awareness

- Snyk offers educational resources, including articles, documentation, and best practices, to help developers improve their understanding of security issues and best practices in coding securely.

#### Trivy

Trivy scans Docker container images for OS and application-level vulnerabilities. It detects critical vulnerabilities within the base operating system of our Docker images or flags insecure configurations within the application setup within the container. Trivy focuses on identifying high-severity vulnerabilities that pose significant risks - it identifies a critical vulnerability within a specific software library or an unpatched component, prompting immediate remediation actions.

Container Image Analysis

- Trivy starts by examining the metadata of container images. It gathers information about the operating system, software packages, and dependencies installed within the image.

Vulnerability Database

- Trivy references the Common Vulnerabilities and Exposures (CVE) database and other vulnerability databases to compare the metadata and software versions found within the container image against known vulnerabilities and security issues.
- Trivy's vulnerability database is regularly updated to include the latest known vulnerabilities, ensuring accurate detection of security flaws.

Vulnerability Detection

- Trivy performs a deep scan of the container image's layers and filesystem, checking each layer and its corresponding packages for vulnerabilities.
- It identifies vulnerabilities in various software packages and libraries (e.g., OS packages, language-specific dependencies) present within the container image.
- Trivy categorizes vulnerabilities based on severity levels (e.g., critical, high, medium, low), providing insights into the potential impact of each vulnerability.

Integration with Container Registries and CI/CD

- Trivy seamlessly integrates with container registries (such as Docker Hub, Amazon ECR, and others) to scan images stored in repositories.
- It can be integrated into Continuous Integration/Continuous Deployment (CI/CD) pipelines, allowing automated scanning of container images at different stages of the development lifecycle.

Actionable Insights and Remediation

- Trivy generates reports detailing identified vulnerabilities, including descriptions, CVE IDs, severity levels, affected package versions, and links to additional information.
- It provides actionable insights and recommendations on how to remediate vulnerabilities, such as suggesting package upgrades, patches, or alternative versions.

Performance and Efficiency

- Trivy is designed for speed and efficiency, offering relatively fast scans, making it suitable for integration into development workflows without causing significant delays.
- It leverages layer-based scanning to optimize performance, examining only the necessary layers and their respective packages for vulnerabilities.

Extensibility and Configuration

- Trivy allows some customization and configuration options, such as excluding certain packages or ignoring specific vulnerabilities based on user-defined policies or requirements.

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
