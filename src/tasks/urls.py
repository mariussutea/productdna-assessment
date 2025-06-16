from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("tasks", views.TaskViewSet, basename="task")
router.register("tags", views.TagViewSet, basename="tag")

app_name = "tasks"

urlpatterns = [
    path("", include(router.urls))
]
