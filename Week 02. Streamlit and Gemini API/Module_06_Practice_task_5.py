from turtle import setup
from google import genai
import os
import streamlit as st 
from dotenv import load_dotenv

# load . env
load_dotenv()

# API Key 
api_key = os.getenv("GEMINI_API_KEY")

# Client setup 
client = genai.Client(api_key=api_key)

st.title("Task 5: Gemini Chatbot App")
st.divider()

# input
question = st.text_input("Hi there! Whare should we start ?")
# button
pressed = st.button("Ask Gemini")


if pressed:
    if question == "":
        st.error("Please enter a question!")
    else:
        with st.spinner("Loading..."):
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=question
            )
            
        st.markdown(response.text)