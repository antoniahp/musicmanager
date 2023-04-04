from django.db import models
from django.utils import timezone

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=150)

class Song(models.Model):
    title = models.CharField(max_length=150)
    picture_url = models.TextField()
    external_url = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    created_date = models.DateTimeField(default=timezone.now)

