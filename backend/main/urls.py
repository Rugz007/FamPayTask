from django.urls import path
from .views import VideosViewSet

urlpatterns = [
    path('create/', VideosViewSet.as_view({'get': 'list_videos'}),
         name='list_videos'),
    path('search/', VideosViewSet.as_view({'post': 'search_videos'}),
         name='search_videos'),
]
