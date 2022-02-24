import subprocess
import os
from pathlib import Path
from uuid import uuid4
import moviepy.editor as me

BASE_DIR = Path(__file__).parent.parent / 'media/video/temp' # temp dir path 

audio_striped_output = BASE_DIR / f'{str(uuid4())}.mp4' # Path for storing audio striped video
output = BASE_DIR / f'{str(uuid4())}.mp4'               # Path for storing merged audio and video
compressed_output = BASE_DIR / f'{str(uuid4())}.mp4'    # Path for storing compressed video

# Function to get audio duration
def audio_length(audio):
    with me.AudioFileClip(audio) as aud:
        duration = aud.duration
    return duration

# Function to get video duration
def video_length(video):
    with me.VideoFileClip(video) as vid:
        duration = vid.duration
    return duration


def convert_video(video, audio):
    #Strip audio from video
    strip_audio = ['ffmpeg', '-i', video, '-c', 'copy', '-an', audio_striped_output]
    subprocess.run(strip_audio, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    #Merge Video and Audio
    #Checking video length and audio length
    if video_length(video) > audio_length(audio):
        merge_audio_and_video = ['ffmpeg', '-i', audio_striped_output, '-i', audio, '-c', 'copy', output]
        subprocess.run(merge_audio_and_video, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        merge_audio_and_video = ['ffmpeg', '-i', audio_striped_output, '-i', audio, '-c', 'copy', '-shortest', output]
        subprocess.run(merge_audio_and_video, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


    # removing audio_striped video from temp directory
    os.remove(audio_striped_output)

    # Compressing the merged video and audio
    compress_video = ['ffmpeg', '-i', output, '-vcodec', 'libx264', '-crf', '28', compressed_output]
    subprocess.run(compress_video, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # removing merged video and audio from temp directory
    os.remove(output)

    # Returning the path of compressed output video
    return compressed_output


