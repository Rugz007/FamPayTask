from .models import APIKey, Video
import os
import googleapiclient.discovery
import googleapiclient.errors
from celery import shared_task
import datetime
from googleapiclient.errors import HttpError
from django.conf import settings

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


@shared_task
def fetch_videos():
    api_key = APIKey.objects.all().first()
    if api_key is None:
        print("No API Key")
        return
    youtube = googleapiclient.discovery.build(
        settings.YOUTUBE_SERVICE_NAME,
        settings.YOUTUBE_API_VERSION,
        developerKey=api_key.key,
    )
    video = Video.objects.all().order_by("-published_at").first()
    if video is not None:
        published_after = video.published_at.replace(tzinfo=None)
    else:
        published_after = datetime.datetime.utcnow() - datetime.timedelta(minutes=60)
    published_after = published_after.isoformat("T") + "Z"
    next_page_token = None
    while True:
        try:
            response = (
                youtube.search()
                .list(
                    part="snippet",
                    maxResults=25,
                    q="gaming",
                    type="video",
                    publishedAfter=published_after,
                    pageToken=next_page_token,
                    order="date",
                )
                .execute()
            )
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
            if "nextPageToken" in response:
                next_page_token = response["nextPageToken"]
            else:
                break
        except HttpError as e:
            if e.resp["status"] == "403":
                print("error")
                if APIKey.objects.all().count() > 1:
                    api_key.delete()
                return

