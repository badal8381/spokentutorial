from uuid import uuid4
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File
from .func import convertToSpeech
from .models import textToSpeech
from .forms import TextForm
import os
import mimetypes


def index(request):
    if request.method == 'POST':
        request_file = request.FILES['text_file']
        # Checking the uploaded file whether it is '.txt' or not
        if request_file.name[-3:] == 'txt':
            voice = request.POST['voice']
            id = str(uuid4())
            form = TextForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.text_id = id
                obj.save()

            obj = textToSpeech.objects.get(text_id=id)
            url = convertToSpeech(obj.text_file.url[1:], voice)
            with url.open(mode='rb') as f:
                obj.speech = File(f, f'{id}.mp3')
                obj.text_file.delete()
                obj.save()

            os.remove(url)
            return render(request, 'tts/test.html', {'data': obj})

        # If uploaded file is not '.txt' then display invalid file format..
        # The validation is checked on server side, because it can be bypassed on client side
        else:
            form = TextForm()
            message = "Invalid File Format, only '.txt' files are Supported.."
            return render(request, 'tts/test.html', {'form': form, 'message': message})

    form = TextForm()
    return render(request, 'tts/test.html', {'form': form})


def download_speech(request, id):
    obj = textToSpeech.objects.get(text_id=id)

    fl_path = obj.speech.url[1:]
    filename = 'speech.mp3'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='audio/mpeg')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
