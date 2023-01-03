from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Conf.forms.Task import TaskForm
from Conf.models.Task import Task
from Conf.serializers.Task import TaskListSerializer
from Main.DefaultViews.GeneralViews import AuthBaseTemplateView, AuthBaseCreateView, AuthBaseUpdateView, AuthBaseDeleteView


class TaskListView(AuthBaseTemplateView):
    title = "List Tasks"
    template_name = 'task/list.html'


class TaskCreateViewAuth(AuthBaseCreateView):
    title = "Create Task"
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')
    template_name = 'task/create.html'


class TaskUpdateView(AuthBaseUpdateView):
    title = "Update Task"
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')
    template_name = 'task/update.html'
    model = Task



class TaskDeleteView(AuthBaseDeleteView):
    title = "Delete Task"
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')
    model = Task


class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]


class NewListView(AuthBaseTemplateView):
    title = "List Tasks 2"
    template_name = 'task/List2.html'