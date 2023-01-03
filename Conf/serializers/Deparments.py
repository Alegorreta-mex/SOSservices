from rest_framework import serializers

from Conf.models.Deparments import Department


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "description",
            "leader",
            "members"
        ]
