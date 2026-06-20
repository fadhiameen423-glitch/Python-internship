import streamlit as st
if "count" not in st.session_state:
    st.session_state["count"]=0

delta_value=0
if st.button("Increment"):
    st.session_state["count"] +=1
    delta_value=1

st.metric("Click count",st.session_state["count"],delta_value)