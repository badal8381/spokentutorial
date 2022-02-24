import os
from uuid import uuid4
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from .func import convert_video
from .models import convertedVideo

vid_ext = ['mp4', 'mov', 'wmv', 'avi', 'mkv']
aud_ext = ['mp3', 'aac', 'ogg', 'wav']


def video(request):
    if request.method == 'POST' and request.FILES:
        video = request.FILES['video']
        audio = request.FILES['audio']
        if video.name[-3:] not in vid_ext and audio.name[-3:] not in aud_ext:
            return render(request, 'videomerge/videomerge.html', {'message': True})

        id = str(uuid4())
        convertedVideo(id=id, video=video, audio=audio).save()

        obj = convertedVideo.objects.get(id=id)
        try:
            url = convert_video(obj.video.url[1:], obj.audio.url[1:])
            with url.open(mode='rb') as f:
                obj.output_video = File(f, f'{id}.mp4')
                obj.video.delete()
                obj.audio.delete()
                obj.save()
            os.remove(url)
        except:
            obj.video.delete()
            obj.audio.delete()
            obj.save()
            obj.delete()
            return render(request, 'videomerge/videomerge.html', {'error': True})

        return render(request, 'videomerge/videomerge.html', {'data': obj})

    return render(request, 'videomerge/videomerge.html')


def download_video(request, id):
    obj = convertedVideo.objects.get(id=id)

    fl_path = obj.output_video.url[1:]
    filename = 'converted_video.mp4'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='video/mp4')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def preview_video(request, id):
    obj = convertedVideo.objects.get(id=id)
    return render(request, 'videomerge/preview.html', {'data': obj})
