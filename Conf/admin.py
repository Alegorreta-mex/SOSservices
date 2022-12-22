from django.contrib import admin

# Register your models here.
from Conf.models.Task import Task
from Conf.models.Users import CustomUser

admin.site.register([CustomUser, Task])
