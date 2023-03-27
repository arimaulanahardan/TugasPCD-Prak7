import streamlit as st
import numpy as np
import cv2
from PIL import Image
from IPython.display import display

st.title("Praktikum 2👋")

uploaded_file_1 = st.file_uploader("Upload an image 1", type=["png", "jpg", "jpeg"])
uploaded_file_2 = st.file_uploader("Upload an image 2", type=["png", "jpg", "jpeg"])

if uploaded_file_1 is not None and uploaded_file_2 is not None:
    img1 = np.frombuffer(uploaded_file_1.read(), np.uint8)
    img1 = cv2.imdecode(img1, cv2.IMREAD_COLOR)
    img2 = np.frombuffer(uploaded_file_2.read(), np.uint8)
    img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["All Image", "Merge Image", "Add Image", "Image Processing", "Bitwise and", "Bitwise or", "Bitwise xor"])

    with tab1:
        newImg1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        newImg2 =  cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        st.markdown("<h1 style='text-align: center; color: white;'>Image 1</h1>", unsafe_allow_html=True)
        st.image(newImg1, use_column_width=True)
        st.markdown("<h1 style='text-align: center; color: white;'>Image 2</h1>", unsafe_allow_html=True)
        st.image(newImg2, use_column_width=True)
    
    with tab2:
        newImg1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        newImg2 =  cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        newImg1 = Image.fromarray(newImg1)
        newImg2 = Image.fromarray(newImg2)

        newImg1 = newImg1.resize((newImg2.size[0], newImg2.size[1]))
        newImg1 = np.array(newImg1)

        newImg = np.hstack((newImg1, newImg2))

        st.markdown("<h1 style='text-align: center; color: white;'>Merge Image</h1>", unsafe_allow_html=True)
        st.image(newImg, use_column_width=True)

    with tab3:
        newImg1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        newImg2 =  cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        newImg1 = Image.fromarray(newImg1)
        newImg2 = Image.fromarray(newImg2)

        newImg1 = newImg1.resize((newImg2.size[0], newImg2.size[1]))
        newImg1 = np.array(newImg1)

        newImg = np.add(newImg1, newImg2)

        st.markdown("<h1 style='text-align: center; color: white;'>Add Image</h1>", unsafe_allow_html=True)
        st.image(newImg, use_column_width=True)

    with tab4:
        newImg1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        newImg2 =  cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        newImg1 = Image.fromarray(newImg1)
        newImg2 = Image.fromarray(newImg2)

        newImg1 = newImg1.resize((newImg2.size[0], newImg2.size[1]))
        newImg1 = np.array(newImg1)

        newImg = np.add(newImg1, newImg2)
        newImg = cv2.cvtColor(newImg, cv2.COLOR_RGB2GRAY)

        st.markdown("<h1 style='text-align: center; color: white;'>Image Processing</h1>", unsafe_allow_html=True)
        st.image(newImg, use_column_width=True)

    with tab5:
        newImg1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        newImg2 =  cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        newImg1 = Image.fromarray(newImg1)
        newImg2 = Image.fromarray(newImg2)

        newImg1 = newImg1.resize((newImg2.size[0], newImg2.size[1]))
        newImg1 = np.array(newImg1)

        newImg = np.bitwise_and(newImg1, newImg2)

        st.markdown("<h1 style='text-align: center; color: white;'>Bitwise and</h1>", unsafe_allow_html=True)
        st.image(newImg, use_column_width=True)
    
    with tab6:
        newImg1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        newImg2 =  cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        newImg1 = Image.fromarray(newImg1)
        newImg2 = Image.fromarray(newImg2)

        newImg1 = newImg1.resize((newImg2.size[0], newImg2.size[1]))
        newImg1 = np.array(newImg1)

        newImg = np.bitwise_or(newImg1, newImg2)

        st.markdown("<h1 style='text-align: center; color: white;'>Bitwise or</h1>", unsafe_allow_html=True)
        st.image(newImg, use_column_width=True)

    with tab7:
        newImg1 =  cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        newImg2 =  cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        newImg1 = Image.fromarray(newImg1)
        newImg2 = Image.fromarray(newImg2)

        newImg1 = newImg1.resize((newImg2.size[0], newImg2.size[1]))
        newImg1 = np.array(newImg1)

        newImg = np.bitwise_xor(newImg1, newImg2)

        st.markdown("<h1 style='text-align: center; color: white;'>Bitwise xor</h1>", unsafe_allow_html=True)
        st.image(newImg, use_column_width=True)
        