from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)



class Task(models.Model):
    class TaskStatus(models.IntegerChoices):
        PENDING = 0, "Pending"
        IN_PROGRESS = 1, "In Progress"
        DONE = 2, "Done"

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256, null=True, blank=True)
    status = models.IntegerField(choices=TaskStatus.choices, default=TaskStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tag", blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


