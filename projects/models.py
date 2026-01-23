from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ProjectDetail(models.Model):
    # Relazione 1:1 con Project
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='details')
    client_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Details for Project: {self.project.name}"