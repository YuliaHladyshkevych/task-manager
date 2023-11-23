# Task Manager

Task Manager is a web application built with Django, designed to help users manage tasks and streamline task assignment within a team or organization.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Task Manager simplifies task organization and delegation. It allows users to create, assign, and monitor tasks, ensuring streamlined communication and efficient task management within teams or projects.

## Features

- **User Management:** Create and manage user accounts, assign roles, and control access levels.
- **Task Creation and Assignment:** Create tasks, assign them to team members, and set deadlines.
- **Status Tracking:** Monitor task progress and status updates.
- **Dashboard:** Get an overview of pending tasks, completed tasks, and ongoing assignments.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/task-manager.git
   
2. **Navigate to the project directory:**
   ```bash
   cd task-manager
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Apply database migrations:**
   ```bash
   python manage.py migrate
5. **Start the development server:**
   ```bash
   python manage.py runserver
6. **Access the application:**
Open a web browser and go to http://127.0.0.1:8000/ to access the Task Manager application.

## Usage

Upon accessing the application, users can:
- Create and manage tasks
- Assign tasks to team members
- Track task progress and status

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. **Fork the repository:** Click the "Fork" button on the top right corner of this repository's page.
   
2. **Clone your fork:** Clone the repository to your local machine using the following command (replace `<your-username>` with your GitHub username):

   ```bash
   git clone https://github.com/<your-username>/task-manager.git

3. **Create Your Feature Branch:** Start working on a new feature by creating a dedicated branch. Choose a descriptive name for the branch, such as `feature/YourFeature`:

   ```bash
   git checkout -b feature/YourFeature

4. **Commit Your Changes:** Make your desired changes to the codebase and commit them:

   ```bash
   git commit -am 'Add some feature'
   
5. **Push To The Branch:** Push your changes to your fork on GitHub:

   ```bash
   git push origin feature/YourFeature

6. **Create A New Pull Request:** Go to the original repository on GitHub and click on the "New Pull Request" button. Provide details about your changes and submit the pull request for review.

Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata data.json`

- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin`
  - Password: `admin123`

Feel free to add more data using admin panel, if needed.
