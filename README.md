# Django Relational Todo List 🚀

> **⚠️ WORK IN PROGRESS** > This project is currently under development as part of my learning journey. New features, improved error handling, and documentation are being added regularly.

This project is a practical implementation of **Many-to-One** relationships in Django, developed during the **Edgemony / AWS re/Start course**. It features a full CRUD (Create, Read, Update, Delete) system for managing projects and their associated tasks.

## 📌 Learning Objectives
- **Modular Architecture:** Separated business logic into `projects` and `tasks` apps.
- **Relational Integrity:** Implemented **Foreign Keys** with `on_delete=models.CASCADE` to ensure data consistency.
- **RESTful API Design:** Developed endpoints using various HTTP methods (GET, POST, PATCH, DELETE).
- **Database Management:** Used **DBeaver** for schema analysis and **Django Migrations** for version control of the database structure.

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

### Projects
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/api/projects/add/` | Create a new project |
| GET | `/api/projects/` | List all available projects |
| DELETE | `/api/projects/delete/<id>/` | Delete a project and all its associated tasks |

### Tasks
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/api/tasks/add/` | Create a task linked to a project |
| GET | `/api/tasks/?project_id=<id>` | List all tasks for a specific project |
| PATCH | `/api/tasks/update/<id>/` | Partially update task title or description |
| DELETE | `/api/tasks/delete/<id>/` | Remove a specific task |