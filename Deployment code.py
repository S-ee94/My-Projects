# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:32:14 2023

@author: seema
"""

import cv2
import streamlit as st
from ultralytics import YOLO
import numpy as np

# Replace the relative path to your weight file
model_path = r"C:\Users\seema\Desktop\Seema - Personal\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\Model Building Codes\YOLOV8x\YoloV8x Client Data\best.pt"

# Setting page layout
st.set_page_config(
    page_title="Object Detection using YOLOv8",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)


# Creating sidebar
with st.sidebar:
    st.header("Image Config")     # Adding header to sidebar
    
    # Model Options
    confidence = float(st.slider(
        "Select Model Confidence", 25, 100, 40)) / 100
    
    

# Creating main page heading
st.title("Object Detection using YOLOv8")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(
        f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
    res = model.predict(image, conf=confidence)
    result_image = res[0].plot()
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image', channels="BGR", use_column_width=True)

    st.image(result_image, caption='Detected Image', channels="BGR", use_column_width=True)
    st.sidebar.write("Total Detected rods:", len(res[0].boxes))

