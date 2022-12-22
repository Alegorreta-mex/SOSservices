from rest_framework import serializers

from Conf.models.Task import Task


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "responsible"
            "date_start",
            "date_close",
            "previous_task"
        ]