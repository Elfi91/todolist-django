from django.urls import path
from tasks import admin
from tasks.views import create_task, add_task_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/add/', create_task),
    path('api/tasks/details/add/', add_task_details),
]