import streamlit as st
import pandas
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

col3,empty_col,col4=st.columns([1.5,0.5,1.5])
df=pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write("[Source Code](https://pythonhow.com)")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write("[Source Code](https://pythonhow.com)")


