from django.urls import path
from tasks import admin
from tasks.views import create_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/add/', create_task)
]