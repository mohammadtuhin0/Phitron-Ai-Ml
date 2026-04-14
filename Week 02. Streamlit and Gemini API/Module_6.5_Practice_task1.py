import streamlit as st 
st.title("Problem 1 - Create a Calculator")
st.divider()

# input 
a = st.number_input("Enter first number: ", value=None)
b = st.number_input("Enter second number: ", value=None)


# operation 
option = st.selectbox(
    "Choose a operation!",
    ("+", "-", "*", "/"),
    index=None
)

# button
click = st.button("Calculate")

if click:
    result = None
    if option == "+":
        result = a+b
    elif option == "-":
        result = a-b
    elif option == "*":
        result = a*b
    elif option == "/":
        if b==0:
            st.error("Cannot divide by zero!")
        else:
            result = a/b
            
    if result is not None:
        st.success(f"Result: {result}")