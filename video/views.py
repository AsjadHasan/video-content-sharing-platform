
"""Views for retrieving and displaying video content."""

from django.views.generic import ListView

from .models import VideoContent


class VideoListView(ListView):
    """Retrieve videos with their related channel information."""

    model = VideoContent
    template_name = "video/video_list.html"
    context_object_name = "videos"

    def get_queryset(self):
        """Return all videos, newest first, with channel data."""
        return (
            VideoContent.objects
            .select_related("channel")
            .order_by("-created_at")
        )
