import streamlit as st
import requests
import json
import cv2
import numpy as np
import io
from PIL import Image


# 创建一个函数来展示图片
def show_image(image_info, caption):
    if isinstance(image_info, str):
        image = Image.open(image_info)
    else:
        image = image_info
    st.image(image, caption=caption, 
             use_column_width=True)


if __name__ == "__main__":

    st.title("物体检测应用")

    uploaded_images = st.file_uploader("上传图像", type=["jpg", "png", "jpeg"], 
                                    accept_multiple_files=True)
    for file in uploaded_images:
        image = Image.open(file)
        st.image(image, caption="上传的图像", use_column_width=True)

        if st.button(f"检测 {file.name}"):
            # 读取上传的文件内容并转换为字节流对象  
            byte_stream = io.BytesIO()  
            image.save(byte_stream, format="PNG")  
            byte_stream = byte_stream.getvalue()  

            # 上传文件到 FastAPI
            url = "http://127.0.0.1:8111/detect/"
            bytes_io = io.BytesIO(file.read())  
            files = {"files": ("example.jpg", byte_stream, "image/jpeg")}
            response = requests.post(url, files=files)

            if response.status_code == 200:
                try:
                    results = response.json()
                    results = np.array(results, dtype=np.uint8).squeeze()
                    results = cv2.cvtColor(results, cv2.COLOR_BGR2RGB)
                    show_image(results, "res")
                except json.decoder.JSONDecodeError:
                    print("无法解析 JSON 数据")
            elif response.status_code == 204:
                print("响应没有内容")
            else:
                print("请求失败，状态码:", response.status_code)
        
        





