import streamlit as st 
st.title("Task 2: Image Gallery App")
st.divider()

images = st.file_uploader("Upload your images :",
                          type= ["jpg", "jpeg", "png"],
                          accept_multiple_files = True)

pressed = st.button("Submit")

if images:
    if not images:
        st.warning("Please upload images!")
    
    elif len(images) > 3:
        st.error("You can upload maximum 3 images only!")
        
    elif len(images) == 3:
        st.success("Exactly 3 images uploaded!")
        
        st.write("### Your images")
        
        cols = st.columns(3)
        
        for i, img in enumerate(images):
            with cols[i]:
                st.image(img)
                
    else:
            st.warning("Please upload exactly 3 images!")
    