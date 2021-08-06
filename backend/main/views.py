from rest_framework import viewsets, status as http_status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, JSONParser
from drf_yasg.utils import swagger_auto_schema
from .serializers import VideoSerializer
from .models import Video


class VideosViewSet(viewsets.ViewSet):
    parser_classes = (FormParser, JSONParser)

    @swagger_auto_schema(responses={200: VideoSerializer})
    def get_videos(self, request):
        """
        Request to list videos
        """
        videos = Video.objects.all().order_by("-published_at")
        if videos.exists():
            serialized = VideoSerializer(videos, many=True)
            return Response(serialized.data, status=http_status.HTTP_200_OK)
        return Response(status=http_status.HTTP_404_NOT_FOUND)
