from django import path
from projects import admin
from projects.views import create_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/project/add', create_project)
]