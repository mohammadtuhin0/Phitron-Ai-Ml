import streamlit as st

st.title("Input your Information", anchor=False)
st.divider()

name = st.text_input("Enter your name: ", placeholder="Type your name...")
print(type(name))


age = st.number_input("Enter your age", value=None, placeholder="Type your age...")


presed = st.button("Enter to confirm", type="primary")

if presed:
    st.write(f"Your name is : {name} and your age is :{age}")


# password
# password = st.text_input("Enter your password: ", type="password")
# print(type(password))
# st.write("Your password is: ", password)

selecetd = st.selectbox("Choose your profession", 
             ("Student", "Employee", "Businessman"),
             index = None,
             accept_new_options = True)

print(type(selecetd))
st.write("You selected", selecetd)