import os
import cohere
import speech_recognition

from dotenv import load_dotenv
from cohere.classify import Example
from moviepy.editor import VideoFileClip

# change the file path later
AUDIO_WAV = "./classification/audio.wav"

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_TAG_ACCEPTANCE = 0.2
PROMPT_FILE = "./classification/examples.txt"

def classify(file_path):

    video = VideoFileClip(file_path)
    video.audio.write_audiofile(AUDIO_WAV)
    transcript = transcribe_audio(AUDIO_WAV)

    prompts = []
    with open(PROMPT_FILE, "r") as prompt_file:
        lines = prompt_file.readlines()
        for i in range(0, len(lines), 2):
            prompts.append(Example(lines[i].rstrip(), lines[i+1].rstrip()))

    labels = []
    co = cohere.Client(API_KEY)
    classifications = co.classify(
        model = "medium",
        inputs=[transcript],
        examples=prompts
    )
    
    for item in classifications.classifications[0].confidence:
        if item.confidence >= BASE_TAG_ACCEPTANCE:
            labels.append(item.label)
    print(labels[0])
    return labels



def transcribe_audio(file_path):
    with speech_recognition.AudioFile(file_path) as audio_file:
        recognizer = speech_recognition.Recognizer()
        audio_data = recognizer.record(audio_file)
        auto_text = recognizer.recognize_google(audio_data)
        return auto_text
