from django.contrib import admin
from django.urls import path
from projects.views import create_project, delete_project, list_projects, add_project_details
from tasks.views import create_task, get_taks_by_project, delete_task, patch_task, put_task, add_task_details


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Project Endpoints (Senza api/)
    path('projects/add/', create_project),
    path('projects/', list_projects),
    path('projects/delete/<int:project_id>/', delete_project),
    path('projects/details/add/', add_project_details), # Nuova rotta 1:1

    # Task Endpoints (Senza api/)
    path('tasks/add/', create_task),
    path('tasks/', get_taks_by_project),
    path('tasks/delete/<int:task_id>/', delete_task),
    path('tasks/update/<int:task_id>/', patch_task),
    path('tasks/full-update/<int:task_id>/', put_task),
    path('tasks/details/add/', add_task_details), 
]