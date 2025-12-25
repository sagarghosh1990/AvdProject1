import streamlit as st
import pandas as pd



st.title("Deploy An App")
st.text_input("Repository")
st.text_input("Branch")
st.text_input("Main File Path")
st.text_input("App URL(optional)")
st.button("Deploy!")
