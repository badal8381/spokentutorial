from django import forms
from .models import textToSpeech

class TextForm(forms.ModelForm):
    class Meta:
        model = textToSpeech
        fields = ['text_file']