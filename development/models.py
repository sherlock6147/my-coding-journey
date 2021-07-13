from django.db import models
from django.db.models.base import Model

# Create your models here.
class ProjectTag(models.Model):
    # project = models.ForeignKey(Project,on_delete=models.CASCADE)
    value = models.CharField("Tag Name",max_length=50)
    bg_color = models.CharField("Background Color",max_length=6)
    def __str__(self):
        return self.value
class Project(models.Model):
    title = models.CharField("Title",max_length=150)
    link = models.CharField("Link to project",max_length=400,null=True,blank=True)
    deployed_link = models.CharField("Link to deployed project",max_length=400,null=True,blank=True)
    description = models.TextField("Description")
    started_on = models.DateField("Starting date")
    public = models.BooleanField("Public")
    tags = models.ManyToManyField(ProjectTag,"Tags")
    def __str__(self):
        return self.title

