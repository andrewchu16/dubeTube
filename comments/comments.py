from datetime import datetime

class Comment:
    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.timestamp = datetime.now()
        self.timestr = self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")