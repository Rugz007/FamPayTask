from celery import shared_task

@shared_task
def fetch_videos():
    return 10