from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Task, Tag


User = get_user_model()


class TasksAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin')

        self.client = APIClient()
        # self.client.login(username=self.user.username, password=self.user.password)
        self.client.force_authenticate(user=self.user)

        self.url = reverse("tasks:task-list")


    def test_create_task_with_single_tag(self):
        post_data = {
            "title": "test title",
            "description": "test description",
            "status": Task.TaskStatus.PENDING,
            "tags": [
                {"name": "home"}
            ]
        }

        response = self.client.post(self.url, post_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.first()

        self.assertEqual(task.title, "test title")
        self.assertEqual(task.tags.count(), 1)

    def test_create_task_then_update(self):
        post_data = {
            "title": "test title",
            "description": "test description",
            "status": Task.TaskStatus.PENDING,
            "tags": [
                {"name": "home"},
                {"name": "personal"}
            ]
        }

        response = self.client.post(self.url, post_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.first()

        self.assertEqual(task.title, "test title")
        self.assertEqual(task.tags.count(), 2)

        # update the task with one changed tag
        post_data = {
            "title": "test title",
            "description": "test description",
            "status": Task.TaskStatus.PENDING,
            "tags": [
                {"name": "home"},
                {"name": "recent"}
            ]
        }

        response = self.client.put(
            reverse("tasks:task-detail", args=[task.pk]), post_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.first()

        self.assertEqual(task.title, "test title")
        self.assertEqual(task.tags.count(), 2)
        self.assertTrue(task.tags.filter(name="recent").exists())
        self.assertEqual(Tag.objects.count(), 3)

    def test_create_task_with_missing_tags_key(self):
        post_data = {
            "title": "test title",
            "description": "test description",
            "status": Task.TaskStatus.PENDING,
        }

        response = self.client.post(self.url, post_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.first()

        self.assertEqual(task.title, "test title")
        self.assertEqual(task.tags.count(), 0)
