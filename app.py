from flask import Flask, render_template, request, url_for
import os
import sys

app = Flask(__name__)

counter = 0

@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")

@app.route("/upload", methods=["GET"])
def upload() -> str:
    return render_template("upload.html")

@app.route("/video_upload", methods=["POST"])
def video_upload() -> str:
    print("files", request.files, file=sys.stdout)
    print("request", request.form, file=sys.stdout)
    if "video-upload" not in request.files:
        return "smh not good 1" #TODO: create a failed template and upload from there
    video = request.files['video-upload']
    print("video", video.content_type, file=sys.stdout)
    video.save(f"video/{counter}.{(video.content_type).split('/')[1]}")
    return "lol ok"