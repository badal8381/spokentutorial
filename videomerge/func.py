import subprocess
import os
from pathlib import Path
from uuid import uuid4
import moviepy.editor as me

BASE_DIR = Path(__file__).parent.parent / 'media/video/temp'

audio_striped_output = BASE_DIR / f'{str(uuid4())}.mp4'
output = BASE_DIR / f'{str(uuid4())}.mp4'
compressed_output = BASE_DIR / f'{str(uuid4())}.mp4'


def audio_length(audio):
    with me.AudioFileClip(audio) as aud:
        duration = aud.duration
    return duration


def video_length(video):
    with me.VideoFileClip(video) as vid:
        duration = vid.duration
    return duration


def convert_video(video, audio):
    # Command of ffmpeg to strip original video of its audio,
    # we get input video from the function parameter 'video' and save resultant video at 'audio_striped_output' Path
    strip_audio = ['ffmpeg', '-i', video, '-c', 'copy', '-an', audio_striped_output]
    # executing the commands using subprocess
    subprocess.run(strip_audio, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Command of ffmpeg to use the new audio and merge it with the video
    # we take input video 'audio_striped_output' and save resultant video at 'output' Path
    if video_length(video) > audio_length(audio):
        merge_audio_and_video = ['ffmpeg', '-i', audio_striped_output, '-i', audio, '-c', 'copy', output]
        # executing the commands using subprocess
        subprocess.run(merge_audio_and_video, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        merge_audio_and_video = ['ffmpeg', '-i', audio_striped_output, '-i', audio, '-c', 'copy', '-shortest', output]
        # executing the commands using subprocess
        subprocess.run(merge_audio_and_video, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


    # After merging the video and audio we dont need the input video 'audio_striped_output'
    # so we delete the input video 'audio_striped_output' using os.remove
    os.remove(audio_striped_output)

    # Command of ffmpeg to compress the resultant file and create a low filesiz
    # we take input video 'output' and save resultant video at 'compressed_output' Path
    compress_video = ['ffmpeg', '-i', output, '-vcodec', 'libx264', '-crf', '28', compressed_output]
    # executing the commands using subprocess
    subprocess.run(compress_video, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # After Compressing the video we dont need the input video 'output'
    # so we delete the input video 'output' using os.remove
    os.remove(output)

    # Finally we return the path of compressed video so that is can be stored in model.
    return compressed_output


