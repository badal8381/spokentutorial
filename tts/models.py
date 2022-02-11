from django.db import models
from uuid import uuid4

class textToSpeech(models.Model):
    text_id = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    text_file = models.FileField(upload_to='audio/temp')
    speech = models.FileField(upload_to='audio')

    def __str__(self):
        return str(self.text_id)


