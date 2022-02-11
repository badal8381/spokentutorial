from pathlib import Path
from uuid import uuid4
from gtts import gTTS
import pyttsx3

speech_path = f'media/audio/temp/{str(uuid4())}.mp3'

def convertToSpeech(file, voice):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')

    with open(file, 'r') as f:
        if voice == 'f':
            engine.setProperty('voice', voices[1].id)
            text = f.read().replace("\n", " ")
            engine.save_to_file(text, speech_path)
            engine.runAndWait()
            return Path(speech_path)

        elif voice == 'm':
            engine.setProperty('voice', voices[0].id)
            text = f.read().replace("\n", " ")
            engine.save_to_file(text, speech_path)
            engine.runAndWait()
            return Path(speech_path)

        # with open(file, 'r') as f:
        #     text = f.read().replace("\n", " ")
        #     speech = gTTS(text, lang='en', slow=False)
        #     speech.save(speech_path)
