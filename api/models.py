from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    total_times = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.IntegerField(None)
    status = models.BooleanField(None)


class Tag(models.Model):
    name = models.CharField(max_length=30)


class TagTask(models.Model):
    id_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)


class MyUser(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    photo = models.CharField(max_length=30)


class TaskUser(models.Model):
    id_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    counter = models.IntegerField()
    last_time = models.DateField()


class Challange(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(None)
    bet_value = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)


class TaskChallange(models.Model):
    id_challange = models.ForeignKey(Challange, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)
