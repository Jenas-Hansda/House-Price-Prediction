import streamlit as st
import joblib

# Load the model with joblib
try:
    with open("house_price_model.pkl", "rb") as f:
        model = joblib.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("House Price Predictor")

# Input fields with validation
area = st.number_input("Area (sq ft)", min_value=0, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
age = st.number_input("Age of the house (years)", min_value=0, value=5)

if st.button("Predict"):
    try:
        # Model expects 2D array-like input
        prediction = model.predict([[area, bedrooms, age]])
        st.success(f"Predicted Price: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")
