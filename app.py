import streamlit as st
import requests

st.title ("streamlit connectivity test")
st.write("connect success")  

databricks_host = "https://dbc-c57904c6-817b.cloud.databricks.com"
try:
  r = requests.get(f"{databricks_host}/api/2.0/clusters/list", timeout=8)
  if r.status_code == 401:
    st.waarning("datbricks reachable but unauthorised")
  elif r.status_code == 200:
    st.success("reachable")
except Exception as e:
  st.error(f"couldnt reach databricks")
