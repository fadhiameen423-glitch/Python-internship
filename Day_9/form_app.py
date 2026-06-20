import streamlit as st
with st.form("Form_age"):
    name=st.text_input("Enter your name: ","Type name here...")
    email=st.text_input("Enter email: ","Type email here...")
    age=st.number_input("Enter age: ",min_value=0,step=1)
    submit_button=st.form_submit_button("Submit")
if submit_button:
    if not name.strip():
        st.error("Name cant be empty")
    elif "@" not in email:
        st.error("Invalid email")
    elif age<0:
        st.error("Invlid age")
    else:
        st.success("Succes! Thank you")