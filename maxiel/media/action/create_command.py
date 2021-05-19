import speech_recognition as sr
import pyttsx3
import pathlib
import os
import sys
from shutil import copyfile
from maxiel_core.tts import speak

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maxiel.settings")
import django

django.setup()
from base.models import CommandElem
from django.core.files import File


class Plugin:
    filename = os.path.basename(__file__)

    engine = pyttsx3.init()
    r = sr.Recognizer()

    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

    def speech_to_text(self, lang=''):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            if lang == '':
                return self.r.recognize_google(audio, language="ru-RU")
            else:
                return self.r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            return "Робот не розчув фразу"
        except sr.RequestError as e:
            return "Помилка сервісу; {0}".format(e)

    def __init__(self, query):
        self.query = query

    def __del__(self):
        print('delete')

    def dev_get(self):
        return {
            'filename': self.filename,
        }

    def run(self):
        dev_scripts_path = f"{pathlib.Path(__file__).parent.parent.parent.parent.absolute()}/dev_scripts/"
        live_scripts_path = f"{pathlib.Path(__file__).parent.absolute()}/"
        name_command = self.get_name_command()
        name_file = self.get_file_command()
        if os.path.isfile(f"{dev_scripts_path}{name_file}.py"):
            copyfile(f"{dev_scripts_path}{name_file}.py", f"{live_scripts_path}{name_file}.py")
            new_command = CommandElem(
                command=name_command,
            )
            new_command.save()
            new_command.script.save(f"{name_file}.py", File(open(f"{live_scripts_path}{name_file}.py", "rb")))
            new_command.save()

    def get_name_command(self):
        speak("Назовите команду")
        input_str = self.speech_to_text()
        speak("Повторите название команды")
        input_str_new = self.speech_to_text()
        if input_str.lower() == input_str_new.lower():
            speak(f"имя команды - {input_str.lower()}")
            return input_str.lower()
        else:
            return self.get_name_command()

    def get_file_command(self):
        speak("Назовите имя файла в директории dev scripts")
        input_str = self.speech_to_text('en-EN')
        speak("Повторите имя файла")
        input_str_new = self.speech_to_text('en-EN')
        if input_str.lower() == input_str_new.lower():
            speak(f"имя файла - {input_str.lower()}")
            return input_str.lower()
        else:
            return self.get_name_command()
