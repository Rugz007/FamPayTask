from django.contrib import admin
from .models import APIKey, Video


# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'channel_title']


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['key']


admin.site.register(Video, VideoAdmin)
admin.site.register(APIKey, APIKeyAdmin)
