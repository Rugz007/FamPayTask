from django.db import models
from django.db.models.base import Model


class Video(models.Model):
    video_id = models.CharField(unique=True,max_length=20,null=True)
    title = models.TextField(default='',null=True)
    description = models.TextField(default='',null=True)
    channel_title = models.CharField(max_length=225,default='',null=True)
    published_at = models.DateTimeField(null=True)
    thumbnail_url = models.URLField(null=True)