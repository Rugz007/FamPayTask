from rest_framework import viewsets, status as http_status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, JSONParser
from drf_yasg.utils import swagger_auto_schema
from .serializers import VideoSerializer
from .models import Video


class VideosViewSet(viewsets.ModelViewSet):
    parser_classes = (FormParser, JSONParser)
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    
    @swagger_auto_schema(responses={200: VideoSerializer})
    def list_videos(self, request):
        """
        Request to list all videos
        """
        videos = Video.objects.all().order_by("-published_at")
        if videos.exists():
            page = self.paginate_queryset(videos)
            if page is not None:
                serialized = VideoSerializer(page, many=True)
                return self.get_paginated_response(serialized.data)
        return Response(status=http_status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={200: VideoSerializer})
    def search_videos(self, request, query):
        """
        Request to search for videos using title and description
        """
        search_list = query.split(" ")
        videos = Video.objects.none()
        for element in search_list:
            temp_videos_title = Video.objects.filter(title__icontains=element)
            temp_videos_description = Video.objects.filter(
                description__icontains=element
            )
            videos = videos | temp_videos_description | temp_videos_title
            videos = videos.union(temp_videos_description).union(temp_videos_title)
        videos = videos.order_by("-published_at")
        page = self.paginate_queryset(videos)
        if page is not None:
            serialized = VideoSerializer(page, many=True)
            return self.get_paginated_response(serialized.data)
        return Response(status=http_status.HTTP_404_NOT_FOUND)
