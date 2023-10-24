import os
import cv2
import numpy as np
import streamlit as st


# 创建一个函数来展示图片
def show_image(image_info, caption):
    if isinstance(image_info, str):
        image = cv2.imread(image_info)
    else:
        image = image_info
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption=caption, use_column_width=True)


# 创建一个函数来展示视频
def show_video(video_info):
    if isinstance(video_info, str):
        video_file = open(video_info, 'rb')
    else:
        video_file = video_info
    
    st.video(video_file)


# Streamlit 应用程序主要代码
def main():
    # 图片信息，包括缩略图、全貌和时间
    images = [
        {"thumbnail": r"D:\workspace\data\dl\test_images\dog_thumbnail.jpg", 
         "full": r"D:\workspace\data\dl\test_images\dog.jpg", 
         "time": "2023-01-01 10:00 AM"},

        {"thumbnail": r"D:\workspace\data\dl\test_images\2007_000175_thumbnail.jpg", 
         "full": r"D:\workspace\data\dl\test_images\2007_000175.jpg", 
         "time": "2023-01-02 11:30 AM"},
    ]

    # 创建一个侧边栏，显示缩略图和时间
    image_options = [f"图片 {i+1}" for i in range(len(images))]
    st.sidebar.header("事件列表")
    selected_image_index = st.sidebar.selectbox("选择图片", image_options)

    for i, img in enumerate(images):
        image_thumbnail = cv2.imread(img["thumbnail"])
        image_thumbnail = cv2.cvtColor(image_thumbnail, cv2.COLOR_BGR2RGB)
        st.sidebar.image(image_thumbnail, 
                         caption=f"图片 {i + 1}", 
                         use_column_width=True)

    # 在主界面上显示选定图片的全貌和时间
    st.title("图片展示")
    # 从选项中获取索引
    selected_index = image_options.index(selected_image_index)
    selected_image = images[selected_index]
    show_image(selected_image["full"], caption=f"时间: {selected_image['time']}")

    up_load_files = st.file_uploader(label="上传样片", 
                               type=['jpg', 'png', 'avi', 'mp4'],
                               accept_multiple_files=True)
    for file in up_load_files:
        if 'image' in file.type:
            data = file.read()
            img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            show_image(img, "上传")
        elif 'video' in file.type:
            data = file.read()
            show_video(data)


if __name__ == "__main__":
    main()