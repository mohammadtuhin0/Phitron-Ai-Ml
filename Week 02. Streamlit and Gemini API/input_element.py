import streamlit as st

st.title("Input your Information", anchor=False)
st.divider()

name = st.text_input("Enter your name: ", placeholder="Type your name...")
print(type(name))

st.write("Your name is :", name)

# number input 
st.divider()

age = st.number_input("Enter your age", value=None, placeholder="Type your age...")
print(type(age))
st.write("Your age is: ", age)

# password
password = st.text_input("Enter your password: ", type="password")
print(type(password))
st.write("Your password is: ", password)