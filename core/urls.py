from django.contrib import admin
from django.urls import path
# Import dall'app Projects
from projects.views import (
    create_project, delete_project, list_projects, add_project_details
)
# Import dall'app Tasks
from tasks.views import (
    create_task, get_taks_by_project, delete_task, 
    patch_task, put_task, add_task_details, attach_tag_to_task
)
# Import dall'app Tags
from tags.views import create_tag, list_tags 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- PROJECTS ---
    path('projects/add/', create_project),
    path('projects/', list_projects),
    path('projects/delete/<int:project_id>/', delete_project),
    path('projects/details/add/', add_project_details),

    # --- TASKS ---
    path('tasks/add/', create_task),
    path('tasks/', get_taks_by_project),
    path('tasks/delete/<int:task_id>/', delete_task),
    path('tasks/update/<int:task_id>/', patch_task),
    path('tasks/full-update/<int:task_id>/', put_task),
    path('tasks/details/add/', add_task_details),
    
    # --- TAGS (Nuova App M:N) ---
    path('tags/add/', create_tag),
    path('tags/', list_tags),
    
    # --- JUNCTION (Il ponte per collegare Task e Tag) ---
    path('tasks/<int:task_id>/add-tag/', attach_tag_to_task),
]