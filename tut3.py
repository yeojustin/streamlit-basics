import streamlit as st
import spacy
nlp = spacy.loaf ("en_core_web_lg")

def extract_entities(ent_types, text)
    results = []
    doc = nlp(text)
    for ent in doc,ent_types:
        if ent in doc.ents:
            results.append((ent.text, ent.label_))

    return (results)


st.title("Lesson 3: Forms in streamlit")
st.sidebar.header("Params")

