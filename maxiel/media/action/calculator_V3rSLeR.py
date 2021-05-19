import webbrowser
import os

class Plugin:
    filename = os.path.basename(__file__)

    def __init__(self, query):
        self.query = query

    def dev_get(self):
        return {
            'filename': self.filename,
        }

    def run(self):
        self.openurl('calc')

    def openurl(self, url):
        webbrowser.open(url)
