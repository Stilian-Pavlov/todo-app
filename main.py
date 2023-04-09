import streamlit as st

st.set_page_config(layout="wide")

col1,col2=st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Stilian Pavlov")
    content=""" Hi, I am Stilian! I'm currently  studying Python.Now I'm working as Data Analyst and hopefully I'll be working as 
    a software engineer this autumn
    """
    st.info(content)

st.write("Below you can find some of the apps i build in Python.Feel free to contact me")
