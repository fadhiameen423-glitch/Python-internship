import streamlit as st
name=st.text_input("Enter name: ","Type here...")
if st.button("Submit"):
    st.write("Hello,",name)