from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(choices=TaskStatus.choices, default=TaskStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tag", blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
