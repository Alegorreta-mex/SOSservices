from django.urls import path

from Conf.views.Deparments import DepartmentCreateListAPIView, DepartmentUpdateDeleteAPIView
from Conf.views.Task import TaskListView, TaskListAPIView, TaskCreateViewAuth, TaskUpdateView, TaskDeleteView, \
    NewListView
from Conf.views.Users import SignUpViewAuth

app_name = 'conf'
urlpatterns = [
    path('accounts/signup/', SignUpViewAuth.as_view(), name='signup'),
    path('tasks/create', TaskCreateViewAuth.as_view(), name='task-create'),
    path('list2', NewListView.as_view(), name='task-list-2'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('api/task/', TaskListAPIView.as_view(), name='api-task-list'),
    path('api/departments/', DepartmentCreateListAPIView.as_view(), name='api-department-list_create'),
    path('api/departments/<int:pk>', DepartmentUpdateDeleteAPIView.as_view(), name='api-department-detail'),
]
