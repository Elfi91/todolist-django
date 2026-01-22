# Django Relational Todo List 🚀

> **⚠️ WORK IN PROGRESS** > This project is currently under development as part of my learning journey. New features, improved error handling, and documentation are being added regularly.

This project is a practical exercise on managing **Many-to-One** (Molti-a-Uno)relationships in Django, developed during the **Edgemony / AWS re/Start** course.

## 📌 Learning Objectives
- Separate business logic into modular apps (`projects` and `tasks`).
- Implement a **Foreign Key** to link each Task to a specific Project.
- Create API endpoints for data insertion using **Postman**.
- Use **DBeaver** for visualization and analysis of the relational database schema.

## 🛠️ Tech stack
- **Backend:** Python 3.x & Django
- **Database:** SQLite (analyzed via DBeaver)
- **Tooling:** VS Code, Bash CLI, Postman

## 🚀 Getting Started (Local Setup)
1. Clone the repository.
2. Create and activate the virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # o .\venv\Scripts\activate su Windows
3. Install Django:
   ```bash
   pip install django
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. Start the development server:
   ```bash
   python manage.py runserver
## 📡 API Endpoints
`POST /api/project/add/`: Creates a new project.

`POST /api/tasks/add/`: Creates a task linked to a project (`requires project_id`).