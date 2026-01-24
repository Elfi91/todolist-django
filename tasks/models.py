from django.db import models
from tags.models import Tag

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    # Relazione 1:N con Project
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tasks')

    #Relazione M:N (Many-to-Many)
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)

    def __str__(self):
        return self.title

class TaskDetail(models.Model):
    # Relazione 1:1 con Task
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='details')
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=50, default='Medium')

    def __str__(self):
        return f"Details for: {self.task.title}"

