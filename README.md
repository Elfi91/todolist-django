# Django Relational Todo List 🚀

> **⚠️ WORK IN PROGRESS** > This project is currently under development as part of my learning journey. New features, improved error handling, and documentation are being added regularly.

This project is a practical implementation of **Many-to-One** and **One-to-One** relationships in Django, developed during the **Edgemony / AWS re/Start course**. It features a full CRUD (Create, Read, Update, Delete) system for managing projects and their associated tasks.

## 📌 Learning Objectives
- **Modular Architecture:** Separated business logic into `projects` and `tasks` apps.
- **Relational Integrity:** Implemented **Foreign Keys** with `on_delete=models.CASCADE` to ensure data consistency.
- **RESTful API Design:** Developed endpoints using various HTTP methods (GET, POST, PU, PATCH and DELETE).
- **Database Management:** Schema visualization via **DBeaver** and version control through **Django Migrations**.

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
3. Install dependencies:
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
| POST | `/projects/add/` | Create a new project |
| GET | `/projects/` | List all available projects |
| DELETE | `/projects/delete/<id>/` | Delete a project and all its associated data |
| POST | `/projects/details/add/` | Add extra details (Client, Start Date) to a project (1:1) |

### Tasks
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/tasks/add/` | Create a task linked to a project |
| GET | `/tasks/?project_id=<id>` | List all tasks for a specific project |
| PATCH | `/tasks/update/<id>/` | Partially update task title or description |
| PUT | `/tasks/full-update/<id>/` | Replace an entire task (Full update) |
| DELETE | `/tasks/delete/<id>/` | Remove a specific task |
| POST | `/tasks/details/add/` | Add extra details (Deadline, Priority) to a task (1:1) |

## 📊 Database Architecture
The following Entity Relationship Diagram (ERD) illustrates the core logic of the application, focusing on the 1:1 and 1:N relationships.

![Project Database Schema](./Todolist-Diagram.png)

### Data Integrity Logic (Cascade Deletion)
As requested, the project implements a robust "Cascade" logic:
- **1:N Relationship:** A single Project can contain multiple Tasks.
- **1:1 Relationships:** Projects and Tasks have their own dedicated detail tables.

- **Behavior** When a **Project** is deleted, Django automatically triggers a chain reaction:
1. The **ProjectDetail** linked to it is removed.
2. All **Tasks** belonging to that project are deleted.
3. All **TaskDetails** associated with those tasks are cleaned up. This ensures the database remains free of "orphan data."