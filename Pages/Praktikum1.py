import streamlit as st
import numpy as np
import cv2
from PIL import Image
from IPython.display import display

st.title("Praktikum 1👋")

upload_file = st.file_uploader("Upload File", type=['jpg', 'png', 'jpeg'])
if upload_file is not None:
    file_bytes = np.asarray(bytearray(upload_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["RGB", "BGR", "Greyscale", "Red", "Green", "Blue"])
    with tab1:
        st.header("RGB")
        st.image(opencv_image, channels="BGR")
        
    with tab2:
        st.header("BGR")
        st.image(opencv_image, channels="RGB")

    with tab3:
        st.header("Greyscale")
        st.image(cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY))
    
    with tab4:
        st.header("Red")
        st.image(opencv_image[:, :, 2])
    
    with tab5:
        st.header("Green")
        st.image(opencv_image[:, :, 1])
    
    with tab6:
        st.header("Blue")
        st.image(opencv_image[:, :, 0])
