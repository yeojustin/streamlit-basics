import streamlit as st

def clean_text(text):
    text = text.replace("`",
    "").replace("-\n",
    "").replace("\n", 
    " ").replace("\n", " ").strip()

    return(text)

st.title("Intro to layout and images")

#sidebar - include population
st.sidebar.image("logo.png", width=100)
st.sidebar.header("Options")

text = st.sidebar.text_area("Paste Text Area")

button1 = st.sidebar.button("Clean Text")

if button1:
    col1,col2 = st.columns(2)

    col1_expander = col1.expander("Expand Original")
    with col1_expander:
        col1_expander.header("Original Text")
        col1_expander.write(text)


    col2.header("Clean Text")
    clean = clean_text(text)
    col2.write(clean)
