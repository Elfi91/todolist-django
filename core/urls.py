"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projects.views import create_project, delete_project, list_projects
from tasks.views import create_task, get_taks_by_project, delete_task, patch_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/add/', create_project),
    path('api/projects/', list_projects),               
    path('api/projects/delete/<int:project_id>/', delete_project),

    path('api/tasks/add/', create_task),
    path('api/tasks/', get_taks_by_project),
    path('api/tasks/delete/<int:task_id>/', delete_task),
    path('api/tasks/update/<int:task_id>/', patch_task),
]
