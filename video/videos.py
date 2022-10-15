

video = []

class Video:
    def __init__(self: object, video_id: str, thumbnail: str, extension: str, title: str, author: str, date: str):
        self.id = video_id
        self.thumbnail = thumbnail
        self.extension = extension
        self.title = title
        self.author = author
        self.date_posted = date 
        self.views = 0
        self.likes = 0
        self.dislikes = 0

def add_video(video_id: str, thumbnail: str, extension: str, title: str, author: str, date: str):
    video.append(Video(video_id, thumbnail, extension, title, author, date))