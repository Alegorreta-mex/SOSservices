from Conf.models import CustomUser
from Conf.models.BaseModels import CommonInfo
from django.db import models


class Department(CommonInfo):
    name = models.CharField(max_length=150)
    description = models.TextField()
    leader = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(CustomUser, related_name='department_members')
