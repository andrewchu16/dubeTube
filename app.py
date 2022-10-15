from datetime import date
from flask import Flask, render_template, request, url_for, redirect, make_response
from Algorithm import recommendations
import os
import qrcode_generator
import sys
import video
import json
import classification

counter = 0 # thing to give each video a unique name
VIDEO_FOLDER = "static/video"
MAX_SEARCH_CHARS = 5

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index() -> str:
    if request.cookies.get('watched videos') is not None:
        cookies = json.loads(request.cookies.get('watched videos'))
    else:
        cookies = []
    videos = recommendations.run_dubeTube_algorithm(video.get_all_videos(), cookies)
    return render_template("index.html", videos=video.get_all_videos())

@app.route("/upload", methods=["GET"])
def upload() -> str:
    return render_template("upload.html")

@app.route("/video_upload", methods=["POST"])
def video_upload() -> str:
    global counter
    print("files", request.files, file=sys.stdout)
    print("request", request.form, file=sys.stdout)
    if ("video-upload" not in request.files) or ("thumbnail-upload" not in request.files) or ("title" not in request.form) or ("author" not in request.form):
        return render_template("upload_fail.html")
    video_file = request.files['video-upload']
    thumbnail = request.files['thumbnail-upload']
    print("video", video_file.content_type, file=sys.stdout)
    extension = (video_file.content_type).split('/')[1]
    video_file.save(f"{VIDEO_FOLDER}/{counter}.{extension}")
    
    print(f"{VIDEO_FOLDER}/{counter}.{extension}", file=sys.stdout)
    tags = classification.classify(f"{VIDEO_FOLDER}/{counter}.{extension}")
    
    if (tags[0] != "Not Nature"):
        thumbnail.save(f"{VIDEO_FOLDER}/{counter}.{thumbnail.content_type.split('/')[1]}")
        video.add_video(
            str(counter), # id
            f"{counter}.{thumbnail.content_type.split('/')[1]}", # thumbnail
            extension,
            request.form["title"], # title
            request.form["author"], # author
            date.today(), # date
            tags # tags
        )
        counter += 1
        return render_template("upload_success.html")
    return render_template("upload_fail.html")

@app.route("/watch", methods=["GET"])
def watch() -> str:
    v_id = request.args.get("id")
    video.increase_views(v_id)
    vid = video.find_by_id(v_id)
    response = make_response(render_template("video.html", vid=vid, qrcode_generator=qrcode_generator))
    cookies = None
    if request.cookies.get('watched videos') is not None:
        cookies = json.loads(request.cookies.get('watched videos'))
    if cookies == None:
        cookies = []
    for tag in vid.tags:
        cookies.append(tag)
    while len(cookies) > 100:
        cookies.pop(0)
    print(cookies)

    response.set_cookie('watched videos', json.dumps(cookies))
    return response

@app.route("/search", methods=["GET"])
def search() -> str:
    query = request.args.get("query")
    if len(query) > MAX_SEARCH_CHARS:
        query = query[0:MAX_SEARCH_CHARS]

    return query

@app.errorhandler(404)
def page_not_found(e) -> str:
    return render_template("404.html")