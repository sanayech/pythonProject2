import streamlit as st
import pickle  # Importing the pickle module for model loading

# Load your trained model
with open('C:\Users\Motty\Desktop\checkpoint\path_to_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
