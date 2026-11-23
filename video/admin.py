
"""Django admin configuration for channels and videos."""

from django.contrib import admin

from .models import Channel, VideoContent


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    """Manage channels through Django Admin."""

    list_display = (
        "id",
        "name",
        "is_channel_verified",
        "subscribers_count",
        "created_at",
    )

    search_fields = ("name",)
    list_filter = ("is_channel_verified",)
    ordering = ("-created_at",)


@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    """Manage video content through Django Admin."""

    list_display = (
        "id",
        "title",
        "channel",
        "views_count",
        "likes_count",
        "created_at",
    )

    search_fields = ("title", "channel__name")
    list_filter = ("channel",)
    ordering = ("-created_at",)
