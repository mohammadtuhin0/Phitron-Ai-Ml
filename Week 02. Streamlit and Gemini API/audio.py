import streamlit as st

st.title("Input your files (audio)", anchor=False)
st.divider()

# from directory
st.audio("audio/Tomake Chai.mp3")

st.divider()

audio_file = st.file_uploader("Enter your image: ",
                 type=['mp3', 'ogg', 'flac', 'mp4'])

print(type(audio_file))

if audio_file:
    st.audio(audio_file)