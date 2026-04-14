import streamlit as st
st.title("Task 3: Audio & Video Player App")
st.divider()


audio = st.file_uploader("Upload your Audio",
                         type = ["mp3", "ogg"])

video = st.file_uploader("Upload your video",
                         type=["mp4", "mkv"])

pressed = st.button("Play")

if pressed:
    if audio is None and video is None:
        st.error("Please upload at least one file!")
        
    else:
        if audio is not None:
            st.audio(audio)
            
        if video is not None:
            st.video(video)