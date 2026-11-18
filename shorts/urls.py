from django.urls import path
from .views import ShortsView, Shortswatchview, MusicView


urlpatterns = [
    path('', ShortsView.as_view(), name='shorts'),
    path('watch/', Shortswatchview.as_view(), name='shorts_watch'),
    path('watch/music/', MusicView.as_view(), name='shorts_music'),
]