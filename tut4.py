import streamlit as st
import spacy

# Caching model needs to be cache in function
@st.cache_data
def load_model(model_name):
    # Load the spaCy model
    nlp = spacy.load("model_name")
    return nlp

nlp = spacy.load("en_core_web_sm")

def extract_entities(ent_types, text):
    results = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, ent.label_))
    return results

# Title of the Streamlit app
st.title("Forms in Streamlit")

# Image on sidebar
st.sidebar.image('logo.png',)

# Sidebar for parameters
st.sidebar.header("Parameter")

# List of entity types to choose from
entity_types = ["PERSON", "ORG", "GPE", "LOC", 
                "DATE", "TIME", "MONEY", "PERCENT", 
                "FAC", "PRODUCT", "EVENT", "LANGUAGE", 
                "LAW", "NORP", "ORDINAL", "QUANTITY", 
                "WORK_OF_ART"]

# Multiselect box in the sidebar for selecting entity types
selected_ent_types = st.sidebar.multiselect("Select entity types:", entity_types)

# Text area for user input
text_input = st.text_area("Enter text to analyze:", height=200)

# Button to extract entities
if st.button("Extract Entities"):
    if text_input:
        entities = extract_entities(selected_ent_types, text_input)
        st.subheader("Extracted Entities")
        if entities:
            for entity, label in entities:
                st.write(f"{entity} ({label})")
        else:
            st.write("No entities found.")
    else:
        st.write("Please enter some text to analyze.")


