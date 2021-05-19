import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
import os
import requests
import urllib.parse
from .comands import command
from maxiel_core.tts import speak
from .stt import stt_ru_offline

PROMPT_LIMIT = 5

class QAS(object):
    engine = pyttsx3.init()
    r = sr.Recognizer()
    mic = sr.Microphone()
    use_micro = False

    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

    def speech_to_text(self):
        pass

    def text_to_speach(self, text):
        # self.engine.setProperty('voice', self.ru_voice_id)
        self.engine.say(text)
        self.engine.runAndWait()

    def check_and_DO_IT(self, text):
        return command(text)

    def speach_dialogflow(self, input):
        headers = {
            'Authorization': 'Bearer 518e905cdced427595af19e0cac0ecfe',
        }
        params = (
            ('v', '20170712'),
            ('query', input),
            ('lang', 'ru'),
            ('sessionId', 'ae8e2fb2-139b-bed9-ab35-f4e4d0a95c30'),
            ('timezone', 'Europe/Kiev'),
        )
        response = requests.get('https://api.dialogflow.com/v1/query?', headers=headers, params=params)
        if response:
            return response
        else:
            return 'Я вас не совсем понимаю!'

    def core_speech(self):
        while True:
            speak("Слушаю вас")
            input = stt_ru_offline()
            # input = self.speech_to_text()
            speak(input)
            if self.check_and_DO_IT(input) == False:
                speach_output = self.speach_dialogflow(input)
                # self.text_to_speach(speach_output.json()['result']['fulfillment']['speech'])
