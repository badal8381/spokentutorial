from django.db import models
import uuid

def file_rename(instance, filename):
    ext = filename.split('.')[-1]
    return f'video/temp/{instance.id}.{ext}'

class convertedVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    video = models.FileField(upload_to=file_rename)
    audio = models.FileField(upload_to=file_rename)
    output_video = models.FileField(upload_to='video')

    def __str__(self):
        return str(self.video_id)
