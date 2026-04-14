import streamlit as st 
st.title("Task 1: Personal Info Card App")
st.divider()

name = st.text_input("Enter your name: ", placeholder="Type your name...")
age = st.number_input("Enter your age", placeholder="Type your age...", value = None) 
professtion = st.selectbox("Choose your profession: ",
                        ("Student", "Employee", "Businessman", "Freelancer"),
                        index = None, accept_new_options= True)
# button
pressed = st.button("Submit", type="primary")

# logic
if pressed:
    if name and age and professtion:
        st.success("All information successfully!")
        
        st.write("### Your information")
        st.write(f"Name : {name}")
        st.write(f"Age : {age}")
        st.write(f"Profession : {professtion}")
    else:
        st.warning("Please fill all the fields!")