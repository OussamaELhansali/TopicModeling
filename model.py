import streamlit as st 
import pickle
import numpy as np 



def load_model():
    with open('trained_pipeline_NLP-0.1.0.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

classifier = load_model()

def show_predict_page():
    st.title("Topic Modeling : NLP")

    st.write("""Write your question in the section below""")
    
    question = st.text_input("Enter a string:", "")


    ok = st.button("Estimate Topic")
    if ok:
        Topic = classifier.predict([question])
        st.subheader("The estimated Topic is:\t \t \t")
        st.markdown(f"<strong><span style='color: cyan; font-size: 1.5em'>{Topic[0]}</span></strong>", unsafe_allow_html=True)


show_predict_page()