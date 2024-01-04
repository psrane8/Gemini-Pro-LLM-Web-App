from dotenv import load_dotenv
#loading the environment variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(input):
    response=model.generate_content(input)
    return response.text

#Streamlit app
st.set_page_config(page_title="Q & A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="question")
submit=st.button("Ask the question")

#On submitClick

if submit:
    response=get_gemini_response(input)
    st.write(response)