from django.db import models

# Create your models here.
class TopProjects(models.Model):
    projects_json = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
