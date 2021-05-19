from gtts import gTTS
import os


def speak(audio_string):
    while True:
        try:
            tts = gTTS(text=audio_string, lang='ru')
            tts.save("audio.mp3")
            break
        except:
            continue
    os.system("mpg321 audio.mp3")
