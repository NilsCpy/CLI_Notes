from datetime import datetime

class Note():

    def __init__(self, title, content):

        self.title = title
        self.content = content
        self.creation = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
