from django.urls import path

from Conf.views.Task import TaskListView, TaskListAPIView, TaskCreateViewAuth, TaskUpdateView, TaskDeleteView
from Conf.views.Users import SignUpViewAuth

app_name = 'task'
urlpatterns = [
    path('accounts/signup/', SignUpViewAuth.as_view(), name='signup'),
    path('tasks/create', TaskCreateViewAuth.as_view(), name='task-create'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('api/task/', TaskListAPIView.as_view(), name='api-task-list'),
]
