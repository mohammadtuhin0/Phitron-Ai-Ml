import streamlit as st
st.title("Task 4: Text Style Explorer")
st.divider()

text = st.text_input("Enter your text :")

if text != "":
    st.divider()
    st.title(text)
    
    st.divider()
    st.header(text)
    
    st.divider()
    st.subheader(text)
    
    st.divider()
    st.text(text)