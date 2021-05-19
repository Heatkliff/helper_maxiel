from vosk import Model, KaldiRecognizer
import pyaudio
import os, json


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



while True:
    print(stt_ru_offline())