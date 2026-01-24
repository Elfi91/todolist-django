"""
Local routing for the Tags app.
"""

from django.urls import path
from .views import create_tag, list_tags

urlpatterns = [
    path('add/', create_tag),
    path('list/', list_tags),
]