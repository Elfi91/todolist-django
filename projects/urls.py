"""
Local routing for the Projects app.
"""

from django.urls import path
from .views import create_project, list_projects, delete_project, add_project_details, get_expiring_projects

urlpatterns = [
    path('add/', create_project),
    path('', list_projects),
    path('delete/<int:project_id>/', delete_project),
    path('details/add/', add_project_details),
    path('expiring-soon/', get_expiring_projects),
]