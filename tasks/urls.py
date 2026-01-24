"""
Local routing for the Tasks app.
"""

from django.urls import path
from .views import create_task, get_tasks_by_project, delete_task, patch_task, put_task, add_task_details, attach_tag_to_task

urlpatterns = [
    path('add/', create_task),
    path('', get_tasks_by_project),
    path('delete/<int:task_id>/', delete_task),
    path('update/<int:task_id>/', patch_task),
    path('full-update/<int:task_id>/', put_task),
    path('details/add/', add_task_details),
    path('<int:task_id>/add-tag/', attach_tag_to_task),
]