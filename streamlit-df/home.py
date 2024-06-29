import streamlit as st
import pandas as pd
# import streamlit_pandas as sp

@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    return df

df = load_data()