import os
from uuid import uuid4
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from videomerge.func import convert_video
from videomerge.models import convertedVideo

vid_ext = ['mp4', 'mov', 'wmv', 'avi', 'mkv']   # Video file extensions
aud_ext = ['mp3', 'aac', 'ogg', 'wav']          # Audio file extensions

# Views to process video and audio merging and compression
def video(request):
    if request.method == 'POST' and request.FILES:
        video = request.FILES['video']
        audio = request.FILES['audio']
        # File validation check
        if video.name[-3:] not in vid_ext and audio.name[-3:] not in aud_ext:
            return render(request, 'videomerge/videomerge.html', {'message': True})

        id = str(uuid4())
        # storing audio and video in the model and saving it to media directory
        convertedVideo(id=id, video=video, audio=audio).save()

        # gettting object with unique id for processing
        obj = convertedVideo.objects.get(id=id)

        # Error handling, if ffmpeg or anything else gives error
        try:
            url = convert_video(obj.video.url[1:], obj.audio.url[1:])
            with url.open(mode='rb') as f:
                obj.output_video = File(f, f'{id}.mp4')
                obj.video.delete()
                obj.audio.delete()
                obj.save()
            os.remove(url)
        # if error occurs the delete uploaded video and audio files and the corresponding object
        except:
            obj.video.delete()
            obj.audio.delete()
            obj.save()
            obj.delete()
            # return the template with error
            return render(request, 'videomerge/videomerge.html', {'error': True})
            
        # return the template with data
        return render(request, 'videomerge/videomerge.html', {'data': obj})
    
    # return the template
    return render(request, 'videomerge/videomerge.html')



# Response function for file downloading
def download_video(request, id):
    # getting the video using id
    obj = convertedVideo.objects.get(id=id)

    # storing file path 
    fl_path = obj.output_video.url[1:]
    filename = 'converted_video.mp4'  # downloadable filename

    # Opening file and serving as response
    fl = open(fl_path, 'rb')
    response = HttpResponse(fl, content_type='video/mp4')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

# View for video preview
def preview_video(request, id):
    # getting the video using id
    obj = convertedVideo.objects.get(id=id)
    # return the template with video preview
    return render(request, 'videomerge/preview.html', {'data': obj})
