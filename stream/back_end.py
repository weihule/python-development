from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import io
import numpy as np
import cv2
from typing import List
from onnx_infer import ONNXInfer, video_infer


app = FastAPI()

@app.post("/detect/")
async def detect_objects_in_image(files: List[UploadFile]):
    oi = ONNXInfer('./yolox_nano.onnx', 416, 416)
    results = []
    for file in files:
        file_content = await file.read()
        image = cv2.imdecode(np.frombuffer(file_content, np.uint8), cv2.IMREAD_COLOR)
        detection_result = oi(image)
        results.append(detection_result.tolist())  # 将 NumPy 数组转换为 Python 列表
        # results.append(detection_result.tobytes())
    # return FileResponse(io.BytesIO(results[0]), media_type="application/octet-stream")
    return JSONResponse(content=results)    # 直接返回 NumPy 数组的 JSON 格式



