# Containers and tab in streamlit

import streamlit as st

tab1,tab2 = st.tabs(["tab1","tab2"])

con = st.container()

with tab2:
    if "counter" not in st.session_state:
        st.session_state.counter=0

    if st.button("up"):
        con.write(st.session_state.counter)
        st.session_state.counter+=1
        

    if st.button("reset"):
        st.session_state.counter=0
        con.write(st.session_state.counter)