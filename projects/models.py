"""
Project Models.
We define the core Project entity and a separate Detail model to keep 
the main table lean. This 1:1 relationship is perfect for optional 
or secondary metadata.
"""

from django.db import models

class Project(models.Model):
    # The name is the only strictly required field for a project to exist.
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'projects'

class ProjectDetail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='details')
    client_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Metadata for: {self.project.name}"
    
    class Meta:
        db_table = 'project_details'