from uuid import uuid4
from gtts import gTTS
import pyttsx3

speech_path =  f'media/audio/temp/{str(uuid4())}.mp3' # Path for storing speech

def convertToSpeech(file, voice):
    #If female selected in html form 
    with open(file, 'r') as f:
        if voice == 'f':
            text = f.read().replace("\n", " ")
            speech = gTTS(text, lang='en', slow=False)
            speech.save(speech_path)
            return speech_path
        
    #If male selected in html form 
        elif voice == 'm':
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1.0)
            text = f.read().replace("\n", " ")
            engine.save_to_file(text, speech_path)
            engine.runAndWait()
            return speech_path
