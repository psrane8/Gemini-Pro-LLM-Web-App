from dotenv import load_dotenv
#loading the environment variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


#Streamlit page
st.set_page_config(page_title="Gemini Pro LLM Image Model")

st.header("Gemini Pro Vision Application")

input=st.text_input("Input: ", key="input")

uploaded_file=st.file_uploader("Choose an image from the device.",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image",use_column_width=True)

submit=st.button("Tell me something about the image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is")
    st.write(response)
