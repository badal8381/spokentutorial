from django.db import models
from uuid import uuid4

class convertedVideo(models.Model):
    video_id = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    video = models.FileField(upload_to='video/temp')
    audio = models.FileField(upload_to='video/temp')
    output_video = models.FileField(upload_to='video')

    def __str__(self):
        return str(self.video_id)
