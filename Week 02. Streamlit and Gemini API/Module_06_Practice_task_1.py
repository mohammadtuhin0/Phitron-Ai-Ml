import streamlit as st 
st.title("Task 1: Personal Info Card App")
st.divider()

name = st.text_input("Enter your name: ", placeholder="Type your name...")
# presed = st.button("Enter to confirm", type="primary")

age = st.number_input("Enter your age", placeholder="Type your age...", value = None)
presed = st.button("Enter to confirm", type="primary")

if presed:
    st.write(f"Your name is {name} and your age is {age}")
    
    
selected = st.selectbox("Choose your profession: ",
                        ("Student", "Employee", "Businessman", "Freelancer"),
                        index = None, accept_new_options= True)

st.write("You selected ", selected)