import streamlit as st
import requests
import time

if "a" not in st.session_state:
    st.session_state.a = 1
if st.button("1증가"):
    st.session_state.a += 1
if st.button("1감소"):
    st.session_state.a -=1
st.write(st.session_state.a)
@st.cache_data

def call(a):
    time.sleep(5)
    url = f"https://jsonplaceholder.typicode.com/posts/{a}"
    response = requests.get(url)
    data = response.json()
    st.title("Fetched JSON Data")
    return data
st.write(call(st.session_state.a))