"""
Core API Dispatcher.
Author: Elisabetta
Style: antirez-inspired (clean routing, modular inclusion).
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The administrative interface.
    path('admin/', admin.site.urls),
    
    # PROJECT DOMAIN
    # Handles project lifecycles, metadata, and deadline analytics.
    path('projects/', include('projects.urls')),
    
    # TASK DOMAIN
    # Manages operational units of work and their specific details.
    path('tasks/', include('tasks.urls')),
    
    # TAG DOMAIN
    # Provides global categorization entities across the system.
    path('tags/', include('tags.urls')),
]