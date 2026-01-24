"""
Tag Model.
A simple entity to categorize tasks. We use 'unique=True' to ensure 
we don't have duplicate categories in our system.
"""
from django.db import models

class Tag(models.Model):
    # Unique name is the core identifier for a tag.
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tags'