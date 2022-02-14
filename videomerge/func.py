import subprocess
import os
from pathlib import Path
from uuid import uuid4

BASE_DIR = Path(__file__).parent.parent / 'media/video/temp'

audio_striped_output = BASE_DIR / f'{str(uuid4())}.mp4'
output = BASE_DIR / f'{str(uuid4())}.mp4'
compressed_output = BASE_DIR / f'{str(uuid4())}.mp4'

def convert_video(video, audio):
    subprocess.run(f"ffmpeg -i {video} -c copy -an {audio_striped_output}")
    subprocess.run(f"ffmpeg -i {audio_striped_output} -i {audio} -c copy {output}")
    subprocess.run(f"ffmpeg -i {output} -vcodec libx264 -crf 28 {compressed_output}")
    os.remove(audio_striped_output)
    os.remove(output)
    return compressed_output
