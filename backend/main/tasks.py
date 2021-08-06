from .models import Video
import os
import googleapiclient.discovery
import googleapiclient.errors
from celery import shared_task
import datetime

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


@shared_task
def fetch_videos():
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name,
        api_version,
        developerKey="AIzaSyBeZGVY1liN5gTtbmvBvudNlZogyWqhgiI",
    )
    video = Video.objects.all().order_by("-published_at").first()
    if video is not None:
        published_after = video.published_at.replace(tzinfo=None)
    else:
        published_after = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)
    published_after = published_after.isoformat("T") + "Z"
    try:
        response = youtube.search().list(
            part="snippet",
            maxResults=25,
            q="cooking",
            type="video",
            publishedAfter=published_after,
        ).execute()
        if len(response["items"]) == 0:
            return
        for video in response["items"]:
            try:
                video = Video.objects.get(video_id=video["id"]["videoId"])
            except:
                video = Video(
                    video_id=video["id"]["videoId"],
                    title=video["snippet"]["title"],
                    description=video["snippet"]["description"],
                    channel_title=video["snippet"]["channelTitle"],
                    thumbnail_url=video["snippet"]["thumbnails"]["default"]["url"],
                    published_at=video["snippet"]["publishTime"],
                )
                video.save()
    except:
        print("Error")
    # if response["nextPageToken"]:
    #     pass

