from flask import Flask, request, render_template, send_file, send_from_directory
from PIL import Image
import moviepy
import os
from moviepy.editor import ImageSequenceClip, VideoFileClip
from pathlib import Path
from datetime import datetime


app = Flask(__name__,
            template_folder='./templates',
            static_folder='./static')

# videos = [
#     {'thumbnail': './static/thumbnail.png',
#      'name': '11_20231213170328-20231213170415_2.mp4',
#      'video_path': 'D:/Video/20231213/Download/11_20231213170328-20231213170415_2.mp4'},
#     {'thumbnail': './static/thumbnail.png',
#      'name': '11_20231213171957-20231213172014_2.mp4',
#      'video_path': 'D:/Video/20231213/Download/11_20231213171957-20231213172014_2.mp4'},
# ]


# @app.route('/')
# def index():
#     return render_template('index.html', videos=videos)


# 设置视频文件夹路径
video_folder = 'D:/Video/20231213/Download'

@app.route('/')
def index():
    # 获取视频文件夹中的文件列表
    videos = get_video_list(video_folder)
    print(videos)
    return render_template('index.html', videos=videos)

@app.route('/get_video/<path:filename>')
def get_video(filename):
    return send_from_directory(video_folder, filename)

def get_video_list(folder):
    # 获取视频文件夹中的视频列表
    videos = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(('.mp4', '.mkv', '.avi')):
                video_path = os.path.join(root, file)
                videos.append({'name': file, 'path': video_path})
    return videos


def test():
    now = datetime.now()
    y = now.year
    m = now.month
    d = now.day
    print(y, type(y), str(m).rjust(2, "0"), d)

    folder_path = r'D:\Video\20231213\Download'
    files = [f for f in Path(folder_path).iterdir()]

    caps = []
    # 生成缩略图
    for file in files:
        if file.suffix in ['.mp4', '.avi', '.mov']:
            # 创建一个VideoFileClip对象
            clip = VideoFileClip(str(file))

            print(type(clip))

            # 使用视频的开始时间点（0秒）作为缩略图的帧
            # clip.save_frame('thumbnail.png', t=0)

    print(caps)


if __name__ == "__main__":
    # 开启debug模式
    app.run(debug=True,
            host="0.0.0.0",
            port=5002)
    # test()




