import streamlit as st 
import os
from dotenv import load_dotenv
from google import genai

# load .env 
load_dotenv()

# API key 
api_key = os.getenv("GEMINI API_KEY")

# client setup 
client = genai.Client(api_key=api_key)

# UI 
st.title("Gemini promot generator")
st.divider()

# Input 
prompt = st.text_input("Enter your prompt:")

# button
clicked = st.button("Generate")

if clicked:
    if prompt == "":
        st.error("Please enter a prompt")
    else:
        with st.spinner("Generating..."):
            response = client.models.generate_content(
                model = "gemini-3-flash-preview",
                contents = prompt
            )
        st.markdown(response.text)