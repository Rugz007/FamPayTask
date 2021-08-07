from django.urls import path
from .views import VideosViewSet

urlpatterns = [
    path('list/', VideosViewSet.as_view({'get': 'list_videos'}),
         name='list_videos'),
    path('search/<str:query>', VideosViewSet.as_view({'get': 'search_videos'}),
         name='search_videos'),
]
