from django.urls import path
from .views import *

urlpatterns = [
    path('create',VideosViewSet.as_view({'get':'get_videos'}),name='listVideos'),
]
