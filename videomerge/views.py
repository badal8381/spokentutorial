import os
from uuid import uuid4
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from .func import convert_video
from .models import convertedVideo
from .forms import VideoForm

vid_ext = ['mp4', 'mov', 'wmv', 'avi', 'mkv']
aud_ext = ['mp3', 'aac', 'ogg', 'wav']

def video(request):
    if request.method == 'POST' and request.FILES:
        video = request.FILES['video'].name
        audio = request.FILES['audio'].name
        if video[-3:] in vid_ext and audio[-3:] in aud_ext:
            form = VideoForm(request.POST, request.FILES)
            id = str(uuid4())
            if form.is_valid():
                obj = form.save(commit=False)
                obj.video_id = id
                obj.save()

            obj = convertedVideo.objects.get(video_id=id)
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
                return render(request, 'videomerge/videomerge.html', {'form':form,'error':True})

            
            return render(request, 'videomerge/videomerge.html', {'form':form, 'data':obj})


        else:
            form = VideoForm()
            message = "Invalid Video or Audio File format..."
            return render(request, 'videomerge/videomerge.html', {'form':form,'message':message})

    form = VideoForm()
    return render(request, 'videomerge/videomerge.html',{'form':form})




def download_video(request, id):
    obj = convertedVideo.objects.get(video_id=id)

    fl_path = obj.output_video.url[1:]
    filename = 'converted_video.mp4'

    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='video/mp4')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def preview_video(request, id):
    obj = convertedVideo.objects.get(video_id=id)
    return render(request, 'videomerge/preview.html', {'data':obj})