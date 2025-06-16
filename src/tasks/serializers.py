from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        validators=[UniqueValidator(queryset=Tag.objects.all())]
    )

    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ("id",)


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ("id", "title", "description", "status", "created_at", "tags")
        read_only_fields = ("id", "created_at",)

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")

        task = Task.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)

            task.tags.add(tag)

        return task
