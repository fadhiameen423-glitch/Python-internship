import streamlit as st
import requests
if "token" not in st.session_state:
    st.session_state.token= None
if "email" not in st.session_state:
    st.session_state.email= None

def logout():
    st.session_state.token = None
    st.session_state.email = None
    st.rerun()

if st.session_state.token:
    st.title("Dashboard")
    st.success(f"Welome {st.session_state.email}")
    st.button("Logout",on_click=logout)
else:
    str.title("Login")
    with st.form("Login_form"):
        email=st.text_input("Enter email: ","Typer here...")
        password=st.text_input("Enter password: ","type here...")
        submit=st.form_submit_button("Login")

    if submit:
        try:
            response=requests.post("http://127.0.0.1:8000/auth/login",
                                   json={"email":email,"password":password}
            )
            if response.status_code==200:
                data=response.json()
                st.session_state.token=data["access_token"]
                st.session_state.email=data["email"]
                st.rerun()
            else:
                error_msg=response.json().get("detail","Login failed")
                st.error(error_msg)
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to backend server")


