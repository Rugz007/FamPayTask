from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "title",
            "description",
            "channel_title",
            "published_at",
            "thumbnail_url",
        ]


class SearchSerializer(serializers.Serializer):
    text = serializers.CharField()
