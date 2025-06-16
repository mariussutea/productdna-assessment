from rest_framework import viewsets, permissions

from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()

        status = self.request.query_params.get("status")
        if status is not None:
            queryset = queryset.filter(status=status)

        tag = self.request.query_params.get("tag")
        if tag is not None:
            queryset = queryset.filter(tags__name=tag)

        return queryset

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
