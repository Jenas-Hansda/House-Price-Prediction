import streamlit as st
import pickle

# Load model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("House Price Predictor")

area = st.number_input("Area (sq ft)", value=1000)
bedrooms = st.number_input("Bedrooms", value=3)
age = st.number_input("Age of the house", value=5)

if st.button("Predict"):
    prediction = model.predict([[area, bedrooms, age]])
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")
