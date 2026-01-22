from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    # "ponte" verso l'altra app:
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title