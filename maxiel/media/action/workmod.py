from __future__ import print_function
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from time import gmtime, strftime, localtime, strptime, mktime
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
import webbrowser
import threading
import os.path
import pickle
import os
from vosk import Model, KaldiRecognizer
import os, json
import pyaudio


def stt_ru_offline():
    model = Model("model")
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            x = json.loads(rec.Result())
            if len(x["text"]):
                return x["text"]
        else:
            # print(rec.PartialResult())
            pass


def speak(audio_string):
    while True:
        try:
            tts = gTTS(text=audio_string, lang='ru')
            tts.save("audio.mp3")
            break
        except:
            continue
    os.system("mpg321 audio.mp3")


SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
GOOGLE_SPREADSHEET_ID = '1-Earn11W3BPfh0zTXlSFSikHb8_n1J_JTfSOaEYaTas'


class TimeTracking(threading.Thread):
    def __init__(self, task_id, name):
        threading.Thread.__init__(self)
        self.task_id = task_id
        self.task_name = name
        self.start_time = 0

    def run(self):
        pass


class Plugin:
    filename = os.path.basename(__file__)

    def __init__(self, query):
        self.r = sr.Recognizer()
        self.query = query
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def __del__(self):
        print('delete')

    def dev_get(self):
        return {
            'filename': self.filename,
        }

    def run(self):
        speak("Рабочий режим включен")
        while True:
            speak("Ожидаю команды")
            input = self.speech_to_text()
            if 'остановить рабочий режим' in str(input).lower():
                break
            elif 'начало работы над задачей' in str(input).lower():
                print(input)
            elif 'конец работы над задачей' in str(input).lower():
                print(input)
            elif 'добавить запись в идеи' in str(input).lower():
                print(input)
            elif 'добавить задачу' in str(input).lower():
                print(input)
            elif 'остановить рабочий режим' in str(input).lower():
                print(input)
        speak("Рабочий режим отключен")

    def add_job_to_table(self):
        """Shows basic usage of the Sheets API.
            Prints values from a sample spreadsheet.
            """

        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=GOOGLE_SPREADSHEET_ID,
                                    range='Jobs!A:B').execute()
        values = result.get('values', [])

        last_row = len(values) + 1
        speak("назовите название задачи")
        input_job_str = stt_ru_offline()
        # input_job_str = self.speech_to_text()

        body = {
            'values': [
                [
                    input_job_str,
                    0
                ]
            ]
        }
        self.service.spreadsheets().values().update(
            spreadsheetId=GOOGLE_SPREADSHEET_ID,
            range=f'Jobs!A{last_row}:B{last_row}',
            valueInputOption='USER_ENTERED',
            body=body).execute()

    def get_range(self):
        # Call the Sheets API
        speak("назовите начало диапазона")
        input_start_int_str = int(self.speech_to_text())
        speak("назовите конец диапазона")
        input_end_int_str = int(self.speech_to_text())
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=GOOGLE_SPREADSHEET_ID,
                                    range=f'Jobs!A{input_start_int_str}:B{input_end_int_str}').execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            return values

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

    def add_note_to_table(self):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=GOOGLE_SPREADSHEET_ID,
                                    range='note!A:A').execute()
        values = result.get('values', [])

        last_row = len(values) + 1
        speak("записываю")
        # input_job_str = stt_ru_offline()
        input_job_str = self.speech_to_text()

        body = {
            'values': [
                [
                    input_job_str,
                ]
            ]
        }
        self.service.spreadsheets().values().update(
            spreadsheetId=GOOGLE_SPREADSHEET_ID,
            range=f'note!A{last_row}:B{last_row}',
            valueInputOption='USER_ENTERED',
            body=body).execute()

    def schedule_task(self):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=GOOGLE_SPREADSHEET_ID,
                                    range='Jobs!A:B').execute()
        values = result.get('values', [])

        last_row = len(values) + 1
        speak("Назовите название задачи")
        # input_job_str = stt_ru_offline()
        input_job_str = self.speech_to_text()
        speak("Назовите дату для выполнения задачи")
        # input_job_str = stt_ru_offline()
        input_job_date_str = self.speech_to_text()

        body = {
            'values': [
                [
                    input_job_str,
                    input_job_date_str
                ]
            ]
        }
        self.service.spreadsheets().values().update(
            spreadsheetId=GOOGLE_SPREADSHEET_ID,
            range=f'plans!A{last_row}:B{last_row}',
            valueInputOption='USER_ENTERED',
            body=body).execute()

    def get_task_id(self, task_name):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=GOOGLE_SPREADSHEET_ID,
                                    range=f'Jobs!A:A').execute()
        values = result.get('values', [])
        print(result)
        print(values)
        for i in range(len(values)):
            if len(values[i]):
                if values[i][0] == task_name:
                    return i + 1
        return False

    def start_job_from_table(self, task_name):
        task_id = self.get_task_id(task_name=task_name)
        current_datetime = strftime("%A, %m/%d/%y %H:%M", localtime())
        sheet = self.service.spreadsheets()
        body = {
            'values': [
                [
                    current_datetime
                ]
            ]
        }
        self.service.spreadsheets().values().update(
            spreadsheetId=GOOGLE_SPREADSHEET_ID,
            range=f'Jobs!C{task_id}:C{task_id}',
            valueInputOption='USER_ENTERED',
            body=body).execute()

    def end_job_from_table(self, task_name):
        task_id = self.get_task_id(task_name=task_name)
        end_datetime = strptime(strftime("%A, %m/%d/%y %H:%M", localtime()), "%A, %m/%d/%y %H:%M")
        end_datetime = datetime.fromtimestamp(mktime(end_datetime))

        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=GOOGLE_SPREADSHEET_ID,
                                    range=f'Jobs!C{task_id}:C{task_id}').execute()
        values = result.get('values', [])
        if values:
            start_datetime = strptime(values[0][0], "%A, %m/%d/%y %H:%M")
            start_datetime = datetime.fromtimestamp(mktime(start_datetime))
            new_result = sheet.values().get(spreadsheetId=GOOGLE_SPREADSHEET_ID,
                                        range=f'Jobs!B{task_id}:B{task_id}').execute()
            new_values = new_result.get('values', [])
            current_hours = float(new_values[0][0])
            hours = current_hours + round((end_datetime - start_datetime).seconds / 3600, 2)
            body = {
                'values': [
                    [
                        hours
                    ]
                ]
            }
            self.service.spreadsheets().values().update(
                spreadsheetId=GOOGLE_SPREADSHEET_ID,
                range=f'Jobs!B{task_id}:B{task_id}',
                valueInputOption='USER_ENTERED',
                body=body).execute()
            body = {
                'values': [
                    [
                        ''
                    ]
                ]
            }
            self.service.spreadsheets().values().update(
                spreadsheetId=GOOGLE_SPREADSHEET_ID,
                range=f'Jobs!C{task_id}:C{task_id}',
                valueInputOption='USER_ENTERED',
                body=body).execute()




test = Plugin('sts')
test.run()
