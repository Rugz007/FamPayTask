from django.db import models
from django.db.models.base import Model
from django.db.models.indexes import Index


class Video(models.Model):
    video_id = models.CharField(unique=True, max_length=20)
    title = models.TextField()
    description = models.TextField()
    channel_title = models.CharField(max_length=225)
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()

    class Meta:
        indexes = [models.Index(fields=["published_at"]),models.Index(fields=["title"])]


class APIKey(models.Model):
    key = models.TextField()

    class Meta:
        verbose_name = "API Key"
