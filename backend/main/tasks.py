import datetime
import googleapiclient.discovery
from celery import shared_task
from .models import APIKey, Video
from googleapiclient.errors import HttpError
from django.conf import settings


@shared_task
def fetch_videos():
    # Fetching an API Key from the database
    api_key = APIKey.objects.all().first()
    if api_key is None:
        print("No API Key. Please add one from Django Admin")
        return
    youtube = googleapiclient.discovery.build(
        settings.YOUTUBE_SERVICE_NAME,
        settings.YOUTUBE_API_VERSION,
        developerKey=api_key.key,
    )

    # Retrieving the time and date from which the fetching of videos should start.
    video = Video.objects.all().order_by("-published_at").first()
    if video is not None:
        published_after = video.published_at.replace(tzinfo=None)
    else:
        published_after = datetime.datetime.utcnow() - datetime.timedelta(minutes=60)
    published_after = published_after.isoformat("T") + "Z"
    next_page_token = None

    # Fetching videos until there is no more further next page tokens
    while True:
        try:
            response = (
                youtube.search()
                .list(
                    part="snippet",
                    maxResults=25,
                    q=settings.YOUTUBE_KEYWORD,
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
                except Video.DoesNotExist:
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
                # Deleting API key which is exhausted until 1 API key is left.
                if APIKey.objects.all().count() >= 1:
                    api_key.delete()
                return
