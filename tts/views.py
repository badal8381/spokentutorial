from uuid import uuid4
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File
from .func import convertToSpeech
from .models import textToSpeech
import os


def index(request):
    if request.method == 'POST' and request.FILES:
        txt = request.FILES['txt']
        # Checking the uploaded file whether it is '.txt' or not
        if txt.name[-3:] != 'txt':
            return render(request, 'tts/tts.html', {'message': True})


        voice = request.POST['voice']
        id = str(uuid4())
        textToSpeech(id=id, text_file=txt).save()

        obj = textToSpeech.objects.get(id=id)
        try:
            url = convertToSpeech(obj.text_file.url[1:], voice)
            with open(url, 'rb') as f:
                obj.speech = File(f, f'{id}.mp3')
                obj.text_file.delete()
                obj.save()

            os.remove(url)
            return render(request, 'tts/tts.html', {'data': obj})
        except:
            obj.text_file.delete()
            obj.save()
            obj.delete()
            return render(request, 'tts/tts.html', {'error': True})

    return render(request, 'tts/tts.html')


def download_speech(request, id):
    obj = textToSpeech.objects.get(id=id)

    fl_path = obj.speech.url[1:]
    filename = 'speech.mp3'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='audio/mpeg')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
