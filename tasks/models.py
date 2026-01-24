"""
Task Models.
Everything here revolves around the Task entity. We use a ForeignKey for 
the 1:N relationship with Project and a ManyToManyField for Tags.
Secondary data is isolated in TaskDetail (1:1).
"""

from django.db import models
from tags.models import Tag

class Task(models.Model):
    # Basic task info. Title is mandatory.
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    # 1:N Relationship: A project can have many tasks.
    # If the project is deleted, all its tasks are wiped (CASCADE).
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tasks')

    # M:N Relationship: Tasks and Tags are independent but connected.
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)

    def __str__(self):
        return self.title

class TaskDetail(models.Model):
    """
    Extended task information. We use a 1:1 link to keep the 
    main Task table fast for high-volume queries.
    """
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='details')
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=50, default='Medium')

    def __str__(self):
        return f"Metadata for: {self.task.title}"