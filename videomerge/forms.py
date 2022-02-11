from django import forms
from .models import convertedVideo

class VideoForm(forms.ModelForm):
    class Meta:
        model = convertedVideo
        fields = ['video', 'audio']