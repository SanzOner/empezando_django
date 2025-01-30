from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=100)



class Task (models.Model):
    titile = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)



class task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)
