import streamlit as st
import pickle

# Load the model (make sure the file exists in your working directory)
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("House Price Predictor")

# Input fields with default values and minimum values to avoid invalid input
area = st.number_input("Area (sq ft)", min_value=0, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
age = st.number_input("Age of the house (years)", min_value=0, value=5)

if st.button("Predict"):
    # Predict expects a 2D array-like input [[feature1, feature2, feature3]]
    prediction = model.predict([[area, bedrooms, age]])
    
    # Display prediction formatted with commas and 2 decimal places
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")
