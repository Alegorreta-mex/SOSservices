from django.db import models
from django.utils import timezone

from Conf.models import CustomUser


class Task(models.Model):
    responsible = models.ForeignKey(CustomUser, related_name="responsibile", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(CustomUser, related_name="created", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    date_start = models.DateField(default=timezone.now)
    date_close = models.DateField()
    previous_task = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)


class TaskDetails(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, related_name="created_by", on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=timezone.now)
    comments = models.TextField()
