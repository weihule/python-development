import streamlit as st
import requests
import json
import cv2
import numpy as np
import io


# 创建一个函数来展示图片
def show_image(image_info, caption):
    if isinstance(image_info, str):
        image = cv2.imread(image_info)
    else:
        image = image_info
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption=caption, use_column_width=True)


st.title("物体检测应用")

uploaded_images = st.file_uploader("上传图像", type=["jpg", "png", "jpeg"], 
                                   accept_multiple_files=True)
for file in uploaded_images:
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="上传的图像", use_column_width=True)

    if st.button("检测"):
        # 将图像发送到 FastAPI 后端进行检测
        # _, image_bytes = cv2.imencode(".jpg", image)
        # print(f"type(image_bytes) = {type(image)} type(image_bytes.tobytes()) = {type(image.tobytes())}")
        # response = requests.post("http://127.0.0.1:8111/detect/", files={"files": file.read()})

        # 上传文件到 FastAPI
        url = "http://127.0.0.1:8111/detect/"
        files = {"files": ("example.jpg", open(r"d:\workspace\data\dl\test_images\001.jpg", "rb"), "image/jpeg")}
        response = requests.post(url, files=files)
        print("response = ", response.status_code)
        if response.status_code == 200:
            try:
                results = response.json()
                results = np.array(results, dtype=np.uint8).squeeze()
                st.write("检测结果:", results)
                show_image(results, "res")
            except json.decoder.JSONDecodeError:
                print("无法解析 JSON 数据")
        elif response.status_code == 204:
            print("响应没有内容")
        else:
            print("请求失败，状态码:", response.status_code)
        
        






