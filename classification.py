import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageOps
import stages;
import tensorflow as tf
import cv2
import numpy as np


def load_model():
    model = tf.keras.models.load_model('./my_model11.h5')
    return model

model = load_model()

def import_and_predict(img_data, model):
    test_img = cv2.resize(img_data,(128,128))
    test_input = test_img.reshape((1,128,128,3))
    return model.predict(test_input).argmax() 
    

def classificationn():
    

    # st.sidebar.header("Classification")

    # userinput = st.sidebar.radio(
    #     'Stages',
    #     ('General', 'Non Demented', 'Very Mild Demented', 'Mild Demented', 'Moderate Demented')
    # )
    result = ""
    
    st.title("Classification of Alzheimers :")
    uploaded_photo = st.file_uploader("Upload a photo", type = ["jpg", "png"])
    print(uploaded_photo)
    if uploaded_photo is None:
        st.write("Please Upload the photo")
    else:
        file_bytes = np.asarray(bytearray(uploaded_photo.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        predictions = import_and_predict(opencv_image, model=model)
        class_names = ["Mild Demented", "Moderate Demented", "Non Demented", "Very Mild Demented"]
        result = class_names[predictions]
        string = "This image is most likely :" + "  " + class_names[predictions]
        st.success(string)


    if result=='Non Demented':
        stages.nonDemented()

    if result=='Very Mild Demented':
        stages.veryMildDemented()
    
    if result=='Mild Demented':
        stages.mildDemented()
    
    if result=='Moderate Demented':
        stages.moderateDemented()
    
    
    #camera_photo = st.camera_input("Take a Photo")
    