#!/usr/bin/env python3
"""
@Filename:    main.py
@Author:      dulanj
@Time:        2021-09-23 11.22
"""
from typing import Optional

import cv2
import numpy as np
from fastapi import Body
from fastapi import FastAPI
from pydantic import Required

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/image/predict")
def authenticate(image_byte_stream: bytes = Body(Required, media_type="application/octet-stream")):
    img = cv2.imdecode(np.frombuffer(image_byte_stream, np.uint8), -1)
    cv2.imwrite("test.jpg", img)
    return {"status_code": "Image saved", "status": "200"}
