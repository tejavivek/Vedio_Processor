from django.db import models

class Video(models.Model):
    title=models.CharField(max_length=255)
    video_file=models.FileField(upload_to='videos/')

class Subtitle(models.Model):
    video=models.ForeignKey(Video, on_delete=models.CASCADE)
    text=models.TextField()
    start_time=models.FloatField()
    end_time=models.FileField()
# Create your models here.
