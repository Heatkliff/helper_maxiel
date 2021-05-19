import os
import webbrowser


class Plugin:
    filename = os.path.basename(__file__)

    def __init__(self, query):
        self.query = query

    def dev_get(self):
        return {
            'filename': self.filename,
        }

    def run(self):
        self.openurl()

    def openurl(self):
        webbrowser.open('https://www.google.com')
