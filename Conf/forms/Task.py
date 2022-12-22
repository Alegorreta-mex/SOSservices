from django.forms import ModelForm

from Conf.models.Task import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
