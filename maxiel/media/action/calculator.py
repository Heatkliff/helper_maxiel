import webbrowser
import os

class Plugin:
    stt = 'калькулятор'
    tts = 'Відкриваю'
    filename = os.path.basename(__file__)

    def dev_get(self):
        return {
        'stt' : self.stt,
        'filename' : self.filename,
        'tts' : self.tts,
        }

    def run(self):
        self.openurl('calc')
        return self.tts

    def openurl(self, url):
        webbrowser.open(url)
