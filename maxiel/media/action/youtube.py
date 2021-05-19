import os
import webbrowser


class Plugin:
    filename = os.path.basename(__file__)

    def __init__(self, query):
        self.query = query

    def __del__(self):
        print('delete')

    def dev_get(self):
        return {
            'filename': self.filename,
        }

    def run(self):
        self.openurl()

    def openurl(self):
        webbrowser.open('https://www.youtube.com')
