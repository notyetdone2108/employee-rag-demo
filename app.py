import streamlit as st
import requests

st.title ("streamlit connectivity test")
st.write("connect success")  

name = st.text_input("enter your name : ")
if name:
    st.success ("your app is fine")
