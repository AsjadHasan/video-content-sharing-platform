
"""URL configuration for the video app."""

from django.urls import path

from .views import VideoListView

app_name = "video"

urlpatterns = [
    path("", VideoListView.as_view(), name="video_list"),
]
