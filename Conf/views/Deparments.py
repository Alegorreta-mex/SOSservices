from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Conf.models.Deparments import Department
from Conf.serializers.Deparments import DepartmentListSerializer


class DepartmentCreateListAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    permission_classes = [IsAuthenticated]


class DepartmentUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    permission_classes = [IsAuthenticated]
