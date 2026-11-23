from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField()
    is_channel_verified = models.BooleanField(default=False)
    subscribers_count = models.IntegerField(default=0)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class VideoContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()
    thumbnail = models.URLField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='videos')
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title