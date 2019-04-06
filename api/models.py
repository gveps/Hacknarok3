from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=30)


class TagTask(models.Model):
    id_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)


class TaskUser(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_verified = models.BooleanField()
    deadline = models.DateField()


