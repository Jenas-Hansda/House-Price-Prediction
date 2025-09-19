import streamlit as st
import pickle
import os

model_path = "house_price_model.pkl"

if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}. Please ensure it is in the repo.")
else:
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    st.title("House Price Predictor")
    area = st.number_input("Area (sq ft)", min_value=0, value=1000)
    bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
    age = st.number_input("Age of the house (years)", min_value=0, value=5)

    if st.button("Predict"):
        prediction = model.predict([[area, bedrooms, age]])
        st.success(f"Predicted Price: ${prediction[0]:,.2f}")
