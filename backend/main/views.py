from rest_framework import viewsets, status as http_status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, JSONParser
from drf_yasg.utils import swagger_auto_schema
from .serializers import SearchSerializer, VideoSerializer
from .models import Video


class VideosViewSet(viewsets.ViewSet):
    parser_classes = (FormParser, JSONParser)

    @swagger_auto_schema(responses={200: VideoSerializer})
    def list_videos(self, request):
        """
        Request to list videos
        """
        videos = Video.objects.all().order_by("-published_at")
        if videos.exists():
            serialized = VideoSerializer(videos, many=True)
            return Response(serialized.data, status=http_status.HTTP_200_OK)
        return Response(status=http_status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(request_body=SearchSerializer,responses={200:VideoSerializer})
    def search_videos(self,request):
        """
        Request to search for videos
        """
        search_list = request.data['text'].split(" ")
        videos = Video.objects.none()
        for element in search_list:
            temp_videos_title = Video.objects.filter(title__icontains=element)
            temp_videos_description = Video.objects.filter(description__icontains=element)
            videos = videos | temp_videos_description | temp_videos_title
            videos = videos.union(temp_videos_description).union(temp_videos_title)
        serialized = VideoSerializer(videos, many=True)
        return Response(serialized.data,status=http_status.HTTP_200_OK) 